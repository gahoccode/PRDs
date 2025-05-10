Directory structure:
└── joelove100-black-litterman/
    ├── README.md
    ├── requirements.txt
    ├── black_litterman/
    │   ├── __init__.py
    │   ├── constants.py
    │   ├── main.py
    │   ├── settings.json
    │   ├── __pycache__/
    │   ├── domain/
    │   │   ├── __init__.py
    │   │   ├── config_handling.py
    │   │   ├── engine.py
    │   │   ├── views.py
    │   │   └── __pycache__/
    │   ├── market_data/
    │   │   ├── __init__.py
    │   │   ├── data_readers.py
    │   │   └── engine.py
    │   └── ui/
    │       ├── __init__.py
    │       ├── allocation_controls.py
    │       ├── chart_settings_control.py
    │       ├── fonts.py
    │       ├── portfolio_chart.py
    │       ├── view_button.py
    │       ├── view_designer_control.py
    │       └── view_manager.py
    ├── resources/
    └── tests/
        ├── test_domain/
        │   ├── test_engine.py
        │   └── test_views.py
        └── test_market_data/
            └── test_engine.py


Files Content:

================================================
FILE: README.md
================================================
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![MIT](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/)
[![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)](https://GitHub.com/Naereen/StrapDown.js/issues/)

# Black-Litterman asset allocation tool

This tool provides a simple python-based GUI application for constructing
multi-asset portfolios based on the **Black-Litterman** framework.

## Theoretical basis

The Black-Litterman asset allocation model allows an investor to construct a portfolio
based around the "market portfolio", but accounting for their own views about future 
market developments.  These views can be specified either as directional views on the
out/under performance of a single asset class, or can be on the relative performance
of one basket of assets against another.

The methodology employed in this tool is taken from 
"*A Step By Step Guide to the Black-Litterman Model*" by Thomas Idzorek.  A more 
theoretical (although still very accessible) justification for the model is 
provided by Charlotta Mankert and Michael J Selier in their 2011 paper 
"*Mathematical Derivation and Practical Implications for the use of the
Black-Litterman Model*".

## Configuring the app

The app can either run using local data or data from the Refinitiv DataStream API. If you are using 
the latter then a credentials file **black_litterman/credentials.json** must be added with a valid 
username and password for the API.

The settings.json file allows you to configure various other parameters of the model, including
the available universe of assets, the start date for the market data, the risk aversion and the 
Black-Litterman tau parameter. Detailed descriptions of these last two parameters are provided in the 
aforementioned academic resources.

## Using the app

![App image](resources/app_example.png)

1) The main chart shows the market portfolio allocation against the Black-Litterman
allocation (if one or more view is defined)

2) The views panel on the left can be used to add new market views up to a maximum 
of 4.  Currently, the app only supports single-asset relative views.

3) The chart can be changed to show the implied expected returns based on the current
market weights and covariances

4) The current calculation date can be changed - by default, this will be the prior business
day.  You can also change the start date, which sets the window over which the covariance matrix
is calculated.

## Configuring views

![View configuration](resources/view_config_example.png)

* The confidence describes how sure you are of a view - this is converted
into a covariance for the purposes of the model, as set out in the Idzorek
paper

* A view can be an absolute directional view on the performance of an asset, or 
a view on the performance of one asset vs another.  Although the Black-Litterman model
allows for views on *baskets* of assets, I have not had time to implement this here
(chiefly due to challenges on the UI side)

* You can select which asset(s) the view applies to - it is perfectly possible to have 
multiple views involving the same asset


================================================
FILE: requirements.txt
================================================
cardano-sdk-market-data==0.0.4
certifi==2020.4.5.1
chardet==3.0.4
dataclasses==0.7
et-xmlfile==1.0.1
idna==2.9
jdcal==1.4.1
numpy==1.18.2
openpyxl==3.0.3
pandas==1.0.3
PySide2==5.14.2
python-dateutil==2.8.1
pytz==2020.1
requests==2.23.0
scipy==1.4.1
shiboken2==5.14.2
six==1.15.0
urllib3==1.25.9
xlrd==1.2.0


================================================
FILE: black_litterman/__init__.py
================================================



================================================
FILE: black_litterman/constants.py
================================================
from typing import List


class Configuration:

    MARKET_DATA = "market_data"
    MARKET_DATA_SOURCE = "source"
    MARKET_DATA_FILE_PATH = "file_path"
    FIRST_DATE = "first_date"
    LAST_DATE = "last_date"
    ASSET_UNIVERSE = "asset_universe"
    CREDENTIALS = "credentials"

    PARAMETERS = "parameters"
    TAU = "tau"
    RISK_AVERSION = "risk_aversion"


class MarketData:

    PRICE_DATA = "price_data"
    MARKET_CAP_DATA = "market_cap_data"

    @classmethod
    def get_data_types(cls) -> List[str]:

        return [cls.PRICE_DATA, cls.MARKET_CAP_DATA]


class Weights:

    MARKET = "Market Weights"
    BLACK_LITTERMAN = "Black-Litterman Weights"



================================================
FILE: black_litterman/main.py
================================================
import os
import json
from PySide2 import QtWidgets
from black_litterman.ui.view_manager import ViewManager
from black_litterman.ui.portfolio_chart import PortfolioChart
from black_litterman.ui.chart_settings_control import ChartSettingsControl
from black_litterman.domain.config_handling import ConfigHandler
from black_litterman.ui.fonts import FontHelper


class BlackLittermanApp(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self._set_engine_from_config()
        self._create_controls()
        self._initialise_controls()
        self._add_event_handlers()
        self._add_controls_to_layout()
        self._size_layout()

    def _set_engine_from_config(self) -> None:

        config_path = os.path.abspath(os.path.dirname(__file__))
        config_handler = ConfigHandler(config_path)
        self._engine = config_handler.build_engine_from_config()

    def _create_controls(self):
        self._main_chart = PortfolioChart()
        self._view_manager = ViewManager({}, self._engine.get_asset_universe())
        self._chart_settings_control = ChartSettingsControl(*self._engine.get_dates())
        self._view_manager.setMaximumWidth(300)
        self._view_manager.setMinimumWidth(300)

    def _initialise_controls(self):
        self._plot_chart()

    def _add_event_handlers(self):

        self._view_manager.view_changed.connect(self._plot_chart)
        self._chart_settings_control.dates_changed.connect(self._plot_chart)
        self._chart_settings_control.chart_type_changed.connect(self._change_chart_type)

    def _add_controls_to_layout(self):
        layout = QtWidgets.QGridLayout()
        title_label = QtWidgets.QLabel("Black Litterman Asset Allocation Tool")
        title_label.setFont(FontHelper.get_title_font())

        layout.addWidget(title_label, 0, 0, 1, 1)
        layout.addWidget(self._main_chart, 1, 0, 1, 1)
        layout.addWidget(self._view_manager, 1, 1, 1, 1)
        layout.addWidget(self._chart_settings_control, 2, 0, 2, 1)

        self.layout = layout
        self.setLayout(self.layout)

    def _size_layout(self):
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 9)
        self.layout.setColumnStretch(1, 1)

    def _plot_chart(self):

        start_date, end_date, chart_type = self._chart_settings_control.get_settings()
        asset_universe = self._engine.get_asset_universe()
        market_weights = self._engine.get_market_weights(end_date)
        implied_returns = self._engine.get_market_returns(start_date, end_date)
        all_views = self._view_manager.get_all_views()
        if all_views.is_empty():
            self._main_chart.draw_charts(asset_universe, implied_returns, chart_type,
                                         market_weights)
        else:
            black_litterman_weights = self._engine.get_black_litterman_weights(all_views, start_date, end_date)
            self._main_chart.draw_charts(asset_universe, implied_returns, chart_type,
                                         market_weights, black_litterman_weights)

    def _change_chart_type(self):
        _, _, chart_type = self._chart_settings_control.get_settings()
        self._main_chart.select_chart(chart_type)

    @staticmethod
    def _read_config():
        config_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "settings.json")
        with open(config_path) as config_file:
            configuration = json.load(config_file)

        return configuration


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication([])
    app.setStyle("fusion")
    blw = BlackLittermanApp()
    blw.setWindowTitle("Black Litterman")
    blw.resize(1000, 500)
    blw.show()
    sys.exit(app.exec_())



================================================
FILE: black_litterman/settings.json
================================================
{
  "market_data" :
  {
    "source": "reuters",
    "file_path": "C:\\Users\\joelo\\Code\\black_litterman_data.xlsx",
    "first_date": "2017-01-02",
    "last_date": "",
    "asset_universe":
    {
      "UK equities": ["FTSE100", 1000],
      "US equities": ["S&PCOMP", 1000],
      "Europe equities": ["DJES50I", 1000],
      "Japan equities": ["TOKYOSE", 1000],
      "UK gov bonds": ["AUKGVAL", 1],
      "US gov bonds": ["AUSGVAL", 1],
      "German gov bonds": ["TBDGVAL", 1],
      "Japan gov bonds": ["AJPGVAL", 1]
    }
  },
  "parameters":
  {
    "tau": 0.05,
    "risk_aversion": 3
  }
}




================================================
FILE: black_litterman/domain/__init__.py
================================================



================================================
FILE: black_litterman/domain/config_handling.py
================================================
import os
import json
import pandas as pd
from datetime import datetime
from typing import Any, Dict
from black_litterman.constants import Configuration
from black_litterman.domain.engine import BLEngine, CalculationSettings
from black_litterman.market_data.data_readers import DataReaderFactory


class ConfigHandler:

    def __init__(self,
                 config_path):

        self._config_path = config_path

    def _read_config(self) -> Dict[str, Any]:

        main_path = os.path.join(self._config_path, "settings.json")
        credentials_path = os.path.join(self._config_path, "credentials.json")
        with open(main_path) as config_file:
            main_configuration = json.load(config_file)

        with open(credentials_path) as credentials_file:
            credentials = json.load(credentials_file)

        main_configuration[Configuration.CREDENTIALS] = credentials
        if not main_configuration[Configuration.MARKET_DATA][Configuration.LAST_DATE]:
            prev_date = (datetime.now() + pd.offsets.BusinessDay(-1)).strftime("%Y-%m-%d")
            main_configuration[Configuration.MARKET_DATA][Configuration.LAST_DATE] = prev_date
        return main_configuration

    def _build_engine(self,
                      config: Dict[str, Any]) -> BLEngine:

        data_reader = DataReaderFactory.get_data_reader(config)
        calc_settings = CalculationSettings.parse_from_config(config)
        engine = BLEngine(data_reader, calc_settings)
        return engine

    def build_engine_from_config(self) -> BLEngine:

        config = self._read_config()
        engine = self._build_engine(config)
        return engine



================================================
FILE: black_litterman/domain/engine.py
================================================
import numpy as np
import pandas as pd
from scipy import optimize
from typing import List, Dict, Any, Tuple, Optional
from dataclasses import dataclass
from black_litterman.market_data.data_readers import BaseDataReader
from black_litterman.domain.views import ViewCollection, View
from black_litterman.constants import Configuration, Weights


@dataclass(frozen=True)
class CalculationSettings:
    tau: float
    risk_aversion: float
    start_date: str
    calculation_date: str
    asset_universe: Dict[str, str]

    @staticmethod
    def parse_from_config(config: Dict[str, Any]) -> "CalculationSettings":

        config_params = config[Configuration.PARAMETERS]
        config_data = config[Configuration.MARKET_DATA]

        calc_settings = CalculationSettings(config_params[Configuration.TAU],
                                            config_params[Configuration.RISK_AVERSION],
                                            config_data[Configuration.FIRST_DATE],
                                            config_data[Configuration.LAST_DATE],
                                            config_data[Configuration.ASSET_UNIVERSE])
        return calc_settings


class BLEngine:

    def __init__(self,
                 data_reader: BaseDataReader,
                 calc_settings: CalculationSettings):

        self._market_data_engine = data_reader.get_market_data_engine(calc_settings.start_date,
                                                                      calc_settings.calculation_date)
        self._calc_settings = calc_settings

    def get_market_weights(self,
                           end_date: Optional[str] = None) -> pd.Series:
        """
        return the implied market clearing weights
        """

        if end_date is None:
            end_date = self._calc_settings.calculation_date

        weights = self._market_data_engine.get_market_weights(end_date)
        weights.name = Weights.MARKET
        return weights

    def get_market_returns(self,
                           start_date: str,
                           end_date: str) -> pd.Series:
        """
        return the implied market clearing expected returns
        """

        return self._market_data_engine.get_implied_returns(start_date, end_date, self._calc_settings.risk_aversion)

    def get_asset_universe(self) -> List[str]:
        """
        return the names of the current available assets from the
        calculation settings
        """

        return list(self._calc_settings.asset_universe.keys())

    def get_dates(self) -> Tuple[str, str]:
        """
        get the start and end date from the calc settings
        """

        return self._calc_settings.start_date, self._calc_settings.calculation_date

    def get_black_litterman_weights(self,
                                    view_collection: ViewCollection,
                                    start_date: str,
                                    end_date: str) -> pd.Series:
        """
        derive target portfolio weights based on the Black-Litterman
        portfolio optimisation model
        """

        # get the market data
        market_weights = self._market_data_engine.get_market_weights(end_date)
        market_cov = self._market_data_engine.get_annualised_cov_matrix(start_date, end_date)

        # get the view specific data
        view_mat = view_collection.get_view_matrix(list(self._calc_settings.asset_universe))
        view_out_performance = view_collection.get_view_out_performances()
        view_cov = self.get_view_covariances_from_confidences(market_weights, market_cov, view_collection)

        # calc BL weights
        bl_weights = self._get_weights(market_weights, market_cov, view_mat, view_cov, view_out_performance)
        bl_weights.name = Weights.BLACK_LITTERMAN
        return bl_weights

    def get_view_covariances_from_confidences(self,
                                              market_weights: pd.Series,
                                              market_covariance: pd.DataFrame,
                                              view_collection: ViewCollection) -> pd.DataFrame:
        """
        build a diagonal covariance matrix from the views
        based on the confidence in each view
        """

        cov_by_view = dict()
        all_views = view_collection.get_all_views()

        for view in all_views:
            var = self._confidence_to_variance(view, market_weights, market_covariance)
            cov_by_view.update({view.id: var})

        var_series = pd.Series(cov_by_view)
        cov_matrix = pd.DataFrame(np.diag(var_series), index=var_series.index, columns=var_series.index)
        return cov_matrix

    def _get_weights(self,
                     market_weights: pd.Series,
                     market_cov: pd.DataFrame,
                     view_matrix: pd.DataFrame,
                     view_cov: pd.DataFrame,
                     view_out_performance: pd.Series) -> pd.Series:
        """
        Black-Litterman calculation to derive target weights
        """

        try:
            mat_1 = (view_cov.divide(self._calc_settings.tau) +
                     view_matrix.dot(market_cov).dot(view_matrix.T))
        except ValueError:
            print("matrix not aligned?")
        mat_1_inv = pd.DataFrame(np.linalg.inv(mat_1.values),
                                 index=mat_1.index, columns=mat_1.index)
        mat_2 = (view_out_performance.divide(self._calc_settings.risk_aversion)
                 - view_matrix.dot(market_cov).dot(market_weights))

        bl_weights = market_weights + view_matrix.T.dot(mat_1_inv).dot(mat_2)
        return bl_weights

    def _get_view_target_weights(self,
                                 view: View,
                                 market_weights: pd.Series,
                                 market_covariance: pd.DataFrame,
                                 view_matrix: pd.DataFrame,
                                 view_out_performance: pd.Series) -> pd.Series:
        """
        get target weights based on the view allocation and
        stated confidence in the view
        """

        zero_view_cov = pd.DataFrame([0], index=[view.id], columns=[view.id])
        full_confidence_weights = self._get_weights(market_weights, market_covariance, view_matrix, zero_view_cov,
                                                    view_out_performance)
        max_weight_difference = full_confidence_weights - market_weights
        target_weights = market_weights.add(view.confidence * max_weight_difference)

        return target_weights

    @staticmethod
    def _get_sum_squares_error(series_1: pd.Series,
                               series_2: pd.Series) -> float:
        """
        get the sum squared errors between two
        series
        """

        diff = series_1.subtract(series_2)
        sum_square = sum([x ** 2 for x in diff])
        return sum_square

    def _confidence_to_variance(self,
                                view: View,
                                market_weights: pd.Series,
                                market_covariance: pd.DataFrame,):
        """
        convert a view confidence level to a variance for
        that view
        """

        view_matrix = view.get_view_data_frame(list(self._calc_settings.asset_universe))
        view_out_performance = pd.Series([view.out_performance], index=[view.id])
        target_weights = self._get_view_target_weights(view, market_weights, market_covariance,
                                                       view_matrix, view_out_performance)

        def _error_vs_target_weights(var) -> float:
            view_cov = pd.DataFrame(var, index=[view.id], columns=[view.id])
            weights_for_cov = self._get_weights(market_weights, market_covariance, view_matrix, view_cov,
                                                view_out_performance)

            return self._get_sum_squares_error(weights_for_cov, target_weights)

        variance = optimize.minimize(_error_vs_target_weights, np.array(0.1), method="BFGS")
        return variance.x[0]



================================================
FILE: black_litterman/domain/views.py
================================================
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List, Optional
from uuid import uuid4


class ViewAllocation:

    def __init__(self,
                 long_asset: str,
                 short_asset: Optional[str] = None):

        self.long_asset = long_asset
        self.short_asset = short_asset

    ABSOLUTE = "Absolute"
    RELATIVE = "Relative"

    @classmethod
    def get_all_view_types(cls):
        return [cls.ABSOLUTE, cls.RELATIVE]

    @property
    def view_type(self):
        if self.short_asset:
            return self.RELATIVE
        else:
            return self.ABSOLUTE


@dataclass(frozen=True)
class View:

    id: str
    name: str
    out_performance: float
    confidence: float
    allocation: ViewAllocation

    @ staticmethod
    def get_new_view_with_defaults(asset: str):
        view_id = uuid4().hex
        name = "New view"
        out_performance = 0
        confidence = 0
        allocation = ViewAllocation(asset)

        return View(view_id, name, out_performance, confidence, allocation)

    def get_view_data_frame(self,
                            asset_universe: List[str]) -> pd.DataFrame:
        view_series = pd.Series([0] * len(asset_universe), index=asset_universe, name=self.id)

        view_series[self.allocation.long_asset] = 1
        if self.allocation.short_asset is not None:
            view_series[self.allocation.short_asset] = -1

        view_data_frame = view_series.to_frame().T
        return view_data_frame


class ViewCollection:

    def __init__(self):

        self._all_views = dict()

    def add_view(self,
                 view: View) -> None:

        self._all_views.update({view.id: view})

    def get_view(self,
                 view_id: int) -> View:

        view = self._all_views[view_id]
        return view

    def get_all_views(self) -> List[View]:

        return list(self._all_views.values())

    def get_view_matrix(self,
                        asset_universe: List[str]) -> pd.DataFrame:

        all_view_data_frames = []
        for view in self._all_views.values():
            view_data_frame = view.get_view_data_frame(asset_universe)
            all_view_data_frames.append(view_data_frame)

        if not all_view_data_frames:
            return pd.DataFrame()
        else:
            view_matrix = pd.concat(all_view_data_frames, axis=0)
            return view_matrix

    def get_view_out_performances(self) -> pd.Series:

        out_performances = pd.Series({view_id: view.out_performance for view_id, view in self._all_views.items()})
        return out_performances

    def get_view_confidence_matrix(self) -> pd.DataFrame:

        uncertainties = pd.Series({view_id: view.confidence for view_id, view in self._all_views.items()})
        cov_matrix = pd.DataFrame(np.diag(uncertainties), index=uncertainties.index, columns=uncertainties.index)
        return cov_matrix

    def is_empty(self):
        return len(self._all_views) == 0




================================================
FILE: black_litterman/market_data/__init__.py
================================================



================================================
FILE: black_litterman/market_data/data_readers.py
================================================
import pandas as pd
from logging import getLogger
from typing import Dict, List
from abc import ABC, abstractmethod
from black_litterman.market_data.engine import MarketDataEngine
from black_litterman.constants import Configuration, MarketData
from cardano.market_data.market_data_client import MarketDataClient

logger = getLogger()


class BaseDataReader(ABC):

    @abstractmethod
    def _read_raw_data(self,
                       start_date: str,
                       end_date: str) -> Dict[str, pd.DataFrame]:
        """
        read in the raw data from
        local source
        """

    @abstractmethod
    def _validate_data(self,
                       raw_data: Dict[str, pd.DataFrame]) -> None:
        """
        check raw data for incorrect
        values
        """

    @abstractmethod
    def _get_formatted_data(self,
                            raw_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        """
        apply type formatting
        to the data
        """

    def get_market_data_engine(self,
                               start_date: str,
                               end_date: str) -> MarketDataEngine:
        """
        read market data an wrap in engine class
        """

        raw_data = self._read_raw_data(start_date, end_date)
        self._validate_data(raw_data)
        formatted_data = self._get_formatted_data(raw_data)
        data_engine = MarketDataEngine(formatted_data[MarketData.PRICE_DATA],
                                       formatted_data[MarketData.MARKET_CAP_DATA])
        return data_engine


class LocalDataReader(BaseDataReader):
    """
    read in data from a local spreadsheet
    """

    def __init__(self,
                 data_file_path):

        self._path = data_file_path

    def _read_raw_data(self,
                       start_date: str,
                       end_date: str) -> Dict[str, pd.DataFrame]:

        raw_data = pd.read_excel(self._path, sheet_name=MarketData.get_data_types(), index_col=0)
        raw_data = raw_data.loc[start_date: end_date, :]
        return raw_data

    def _validate_data(self, raw_data: Dict[str, pd.DataFrame]) -> None:

        pass
        # TODO: should add in some validation here

    def _get_formatted_data(self, raw_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:

        for data in raw_data.values():
            data.index = pd.to_datetime(data.index)

        return raw_data


class SqlDataReader(BaseDataReader):
    """
    read in data from SQL server database
    """

    def _read_raw_data(self,
                       start_date: str,
                       end_date: str):
        raise NotImplementedError()

    def _validate_data(self,
                       raw_data: Dict[str, pd.DataFrame]) -> None:
        raise NotImplementedError()

    def _get_formatted_data(self,
                            raw_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:
        raise NotImplementedError()


class ReutersDataReader(BaseDataReader):
    """
    read in data from the Thompson Reuters
    market data API
    """

    def __init__(self,
                 credentials: Dict[str, str],
                 tickers: Dict[str, str]):
        self._mdc = MarketDataClient(credentials=credentials)
        self._tickers = tickers

    def _read_raw_data(self,
                       start_date: str,
                       end_date: str) -> Dict[str, pd.DataFrame]:

        n = len(self._tickers)
        tickers = [v[0] for v in self._tickers.values()]

        price_requests = list(zip(tickers, ["PI"] * n, [start_date] * n, [end_date] * n))
        price_requests = pd.DataFrame(price_requests, columns=self._mdc.get_reuters_input_headers())
        self._mdc.add_reuters_data(price_requests)

        market_cap_requests = list(zip(tickers, ["X(MV)~GBP"] * n, [start_date] * n, [end_date] * n))
        market_cap_requests = pd.DataFrame(market_cap_requests, columns=self._mdc.get_reuters_input_headers())
        self._mdc.add_reuters_data(market_cap_requests)

        raw_data = self._mdc.get_data_as_dataframe()
        price_data = raw_data[raw_data["field"] == "PI"]
        market_cap_data = raw_data[raw_data["field"] == "X(MV)~GBP"]
        return {MarketData.PRICE_DATA: price_data, MarketData.MARKET_CAP_DATA: market_cap_data}

    def _validate_data(self, raw_data: Dict[str, pd.DataFrame]) -> None:
        # TODO: need to add some market data validation
        pass

    def _get_formatted_data(self, raw_data: Dict[str, pd.DataFrame]) -> Dict[str, pd.DataFrame]:

        rename = {v[0]: k for k, v in self._tickers.items()}
        cap_scalings = {ticker: value[1] for ticker, value in self._tickers.items()}

        all_formatted_data = {}
        for data_type, data in raw_data.items():
            formatted_data = pd.pivot_table(data, columns="ticker", index="date", values="value")
            formatted_data.index = pd.to_datetime(formatted_data.index)
            formatted_data.rename(columns=rename, inplace=True)
            all_formatted_data.update({data_type: formatted_data})

        all_formatted_data[MarketData.MARKET_CAP_DATA] *= cap_scalings

        return all_formatted_data


class DataReaderFactory:

    SOURCE_LOCAL = "local"
    SOURCE_SQL = "sql"
    SOURCE_REUTERS = "reuters"

    @classmethod
    def get_valid_sources(cls) -> List[str]:

        return [cls.SOURCE_LOCAL, cls.SOURCE_SQL]

    @classmethod
    def get_data_reader(cls,
                        config: Dict) -> BaseDataReader:

        config_data = config[Configuration.MARKET_DATA]
        data_source = config_data.get(Configuration.MARKET_DATA_SOURCE, "Not Defined")

        if data_source == cls.SOURCE_LOCAL:
            return LocalDataReader(config_data[Configuration.MARKET_DATA_FILE_PATH])
        elif data_source == cls.SOURCE_SQL:
            return SqlDataReader()
        elif data_source == cls.SOURCE_REUTERS:
            return ReutersDataReader(config[Configuration.CREDENTIALS],
                                     config_data[Configuration.ASSET_UNIVERSE])
        else:
            err_msg = f"Data source '{data_source}' is not recognised - valid sources " \
                f"are {', '.join(cls.get_valid_sources())}"
            logger.error(err_msg)
            raise ValueError(err_msg)



================================================
FILE: black_litterman/market_data/engine.py
================================================
import pandas as pd


class MarketDataEngine:

    def __init__(self,
                 price_data: pd.DataFrame,
                 market_cap_data: pd.DataFrame) -> None:

        self._returns_data = price_data.pct_change(1)
        self._market_cap_data = market_cap_data

    def get_annualised_cov_matrix(self,
                                  start_date: str,
                                  end_date: str):
        """
        get cov matrix based on returns for the
        given dates (inclusive)
        """

        date_mask = (self._returns_data.index >= start_date) & (self._returns_data.index <= end_date)
        returns_for_dates = self._returns_data[date_mask]
        covariance_for_dates = returns_for_dates.cov() * 250
        return covariance_for_dates

    def get_market_weights(self,
                           selected_date: str) -> pd.Series:
        """
        get market-cap weights for instruments based
        on index market caps
        """

        market_cap_for_date = self._market_cap_data[self._market_cap_data.index <= selected_date].iloc[-1, :]
        market_weights = market_cap_for_date / market_cap_for_date.sum()
        return market_weights

    def get_implied_returns(self,
                            start_date: str,
                            end_date: str,
                            risk_aversion: float) -> pd.Series:
        """
        get the market clearing returns for the given
        level of risk aversion
        """

        cov_matrix = self.get_annualised_cov_matrix(start_date, end_date)
        market_weights = self.get_market_weights(end_date)
        market_returns = cov_matrix.dot(market_weights).mul(risk_aversion)

        return market_returns



================================================
FILE: black_litterman/ui/__init__.py
================================================



================================================
FILE: black_litterman/ui/allocation_controls.py
================================================
from PySide2 import QtWidgets
from typing import List
from black_litterman.domain.views import ViewAllocation


class AllocationControlAbsolute(QtWidgets.QWidget):

    def __init__(self,
                 allocation: ViewAllocation,
                 asset_universe: List[str]):

        super().__init__()
        self._create_controls()
        self._initialise_controls(allocation, asset_universe)
        self._add_controls_to_layout()
        self._size_layout()

    def _create_controls(self) -> None:

        self._long_asset_combo = QtWidgets.QComboBox()
        self._long_asset_combo.setMinimumHeight(30)

    def _initialise_controls(self,
                             allocation: ViewAllocation,
                             asset_universe: List[str]) -> None:

        self._long_asset_combo.addItems(asset_universe)
        self._long_asset_combo.setCurrentText(allocation.long_asset)

    def _add_controls_to_layout(self):

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        # add main controls
        self.layout.addWidget(self._long_asset_combo, 0, 1)

        # add label controls
        self.layout.addWidget(QtWidgets.QLabel("Long asset:"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel(""), 1, 0)

    def _size_layout(self):

        self.layout.setColumnStretch(0, 2)
        self.layout.setColumnStretch(1, 10)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 10)

    def get_allocation(self):
        return ViewAllocation(self._long_asset_combo.currentText(), None)


class AllocationControlRelative(QtWidgets.QWidget):

    def __init__(self,
                 allocation: ViewAllocation,
                 asset_universe: List[str]):

        super().__init__()
        self._create_controls()
        self._initialise_controls(allocation, asset_universe)
        self._add_controls_to_layout()
        self._size_layout()

    def _create_controls(self) -> None:

        self._long_asset_combo = QtWidgets.QComboBox()
        self._long_asset_combo.setMinimumHeight(30)

        self._short_asset_combo = QtWidgets.QComboBox()
        self._short_asset_combo.setMinimumHeight(30)

    def _initialise_controls(self,
                             allocation: ViewAllocation,
                             asset_universe: List[str]) -> None:

        self._long_asset_combo.addItems(asset_universe)
        self._long_asset_combo.setCurrentText(allocation.long_asset)

        self._short_asset_combo.addItems(asset_universe)
        self._short_asset_combo.setCurrentIndex(0)

    def _add_controls_to_layout(self):

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        # add main controls
        self.layout.addWidget(self._long_asset_combo, 0, 1)
        self.layout.addWidget(self._short_asset_combo, 1, 1)

        # add label controls
        self.layout.addWidget(QtWidgets.QLabel("Long asset:"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("Short asset:"), 1, 0)
        self.layout.addWidget(QtWidgets.QLabel(""), 2, 0)

    def _size_layout(self):

        self.layout.setColumnStretch(0, 2)
        self.layout.setColumnStretch(1, 10)
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 10)

    def get_allocation(self):
        return ViewAllocation(self._long_asset_combo.currentText(),
                              self._short_asset_combo.currentText())


if __name__ == "__main__":

    import sys
    from PySide2 import QtGui

    app = QtWidgets.QApplication([])
    app.setFont(QtGui.QFont("Arial", 10))

    v = ViewAllocation("asset_1", "asset_2")
    au = ["asset_1", "asset_2", "asset_3", "asset_4"]
    widget = AllocationControlRelative(v, au)
    widget.setWindowTitle("Add new view")
    widget.resize(350, 200)
    widget.show()

    sys.exit(app.exec_())



================================================
FILE: black_litterman/ui/chart_settings_control.py
================================================
from typing import Tuple
from datetime import datetime
import pandas as pd
from PySide2 import QtWidgets, QtCore
from black_litterman.ui.fonts import FontHelper


class ChartTypes:

    WEIGHTS = "weights"
    RETURNS = "returns"

    @classmethod
    def get_chart_types(cls):
        return [cls.WEIGHTS, cls.RETURNS]


class ChartSettingsControl(QtWidgets.QWidget):

    dates_changed = QtCore.Signal()
    chart_type_changed = QtCore.Signal()

    def __init__(self,
                 start_date: str,
                 end_date: str):

        super().__init__()
        self._create_controls()
        self._initialise_controls(start_date, end_date)
        self._add_event_handlers()
        self._add_controls_to_layout()
        self._size_layout()
        self._set_control_style()

    def _create_controls(self):

        self._chart_type_combo = QtWidgets.QComboBox()
        self._chart_type_combo.setMaximumWidth(100)

        self._start_date_edit = QtWidgets.QDateEdit()
        self._start_date_edit.setMaximumWidth(100)

        self._end_date_edit = QtWidgets.QDateEdit()
        self._end_date_edit.setMaximumWidth(100)

    def _initialise_controls(self,
                             start_date: str,
                             end_date: str):

        max_start_date = pd.to_datetime(end_date) - pd.offsets.MonthEnd(3)
        min_end_date = pd.to_datetime(start_date) + pd.offsets.MonthEnd(3)

        self._start_date_edit.setMinimumDate(QtCore.QDate.fromString(start_date, "yyyy-MM-dd"))
        self._start_date_edit.setDate(QtCore.QDate.fromString(start_date, "yyyy-MM-dd"))
        self._start_date_edit.setMaximumDate(QtCore.QDate.fromString(max_start_date.strftime("%Y-%m-%d")))

        self._end_date_edit.setMinimumDate(QtCore.QDate.fromString(min_end_date.strftime("%Y-%m-%d")))
        self._end_date_edit.setDate(QtCore.QDate.fromString(end_date, "yyyy-MM-dd"))
        self._end_date_edit.setMaximumDate(QtCore.QDate.fromString(end_date, "yyyy-MM-dd"))

        self._chart_type_combo.addItems(ChartTypes.get_chart_types())
        self._chart_type_combo.setCurrentText(ChartTypes.WEIGHTS)

    def _add_event_handlers(self):

        self._start_date_edit.editingFinished.connect(self._start_date_updated)
        self._end_date_edit.editingFinished.connect(self._end_date_updated)
        self._chart_type_combo.currentTextChanged.connect(self._chart_type_changed)

    def _add_controls_to_layout(self):

        self._layout = QtWidgets.QGridLayout()
        self.setLayout(self._layout)

        combo_label = QtWidgets.QLabel("Show:")
        combo_label.setMaximumWidth(35)
        self._layout.addWidget(combo_label, 0, 0)
        self._layout.addWidget(self._chart_type_combo, 0, 1)

        start_date_label = QtWidgets.QLabel("History start:")
        start_date_label.setMaximumWidth(75)
        self._layout.addWidget(start_date_label, 0, 2)
        self._layout.addWidget(self._start_date_edit, 0, 3)

        end_date_label = QtWidgets.QLabel("Calculation Date:")
        end_date_label.setMaximumWidth(105)
        self._layout.addWidget(end_date_label, 0, 4)
        self._layout.addWidget(self._end_date_edit, 0, 5)

    def _size_layout(self):

        self._layout.setColumnMinimumWidth(0, 50)
        self._layout.setColumnMinimumWidth(1, 50)
        self._layout.setColumnMinimumWidth(2, 50)
        self._layout.setColumnMinimumWidth(3, 50)
        self._layout.setColumnMinimumWidth(4, 50)
        self._layout.setColumnMinimumWidth(5, 50)

    def _set_control_style(self):

        self._chart_type_combo.setFont(FontHelper.get_text_font())
        self._start_date_edit.setFont(FontHelper.get_text_font())
        self._end_date_edit.setFont(FontHelper.get_text_font())

    def _start_date_updated(self):

        new_start_date = self._start_date_edit.date().toPython()
        new_max_end_date = new_start_date - pd.offsets.MonthEnd(3)
        self._end_date_edit.setMaximumDate(QtCore.QDate.fromString(new_max_end_date.strftime("%Y-%m-%d")))
        self.dates_changed.emit()

    def _end_date_updated(self):

        new_end_date = self._end_date_edit.date().toPython()
        new_min_start_date = new_end_date + pd.offsets.MonthEnd(3)
        self._start_date_edit.setMinimumDate(QtCore.QDate.fromString(new_min_start_date.strftime("%Y-%m-%d")))
        self.dates_changed.emit()

    def _chart_type_changed(self):
        self.chart_type_changed.emit()

    def get_settings(self) -> Tuple[str, str, str]:

        start_date = self._start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self._end_date_edit.date().toString("yyyy-MM-dd")
        chart_type = self._chart_type_combo.currentText()

        return start_date, end_date, chart_type



================================================
FILE: black_litterman/ui/fonts.py
================================================
from PySide2 import QtGui


class FontHelper:

    @staticmethod
    def get_title_font():

        font = QtGui.QFont("Calibri", 14, QtGui.QFont.Bold)
        return font

    @staticmethod
    def get_text_font():
        font = QtGui.QFont("Calibri", 8)
        return font



================================================
FILE: black_litterman/ui/portfolio_chart.py
================================================
import math
import pandas as pd
from typing import List, Optional
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCharts import QtCharts
from black_litterman.ui.chart_settings_control import ChartTypes


class PortfolioChart(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self._create_controls()
        self._add_controls_to_layout()

    def _create_controls(self) -> None:

        self._weights_chart_view = QtCharts.QChartView()
        self._returns_chart_view = QtCharts.QChartView()

    def _add_controls_to_layout(self) -> None:

        self._chart_stack = QtWidgets.QStackedLayout()
        self._chart_stack.addWidget(self._weights_chart_view)
        self._chart_stack.addWidget(self._returns_chart_view)

        self._layout = QtWidgets.QGridLayout()
        self._layout.addLayout(self._chart_stack, 0, 0)
        self.setLayout(self._layout)

    def select_chart(self,
                     selected_chart_type: str) -> None:

        selected_index = self._get_index_for_chart_type(selected_chart_type)
        self._chart_stack.setCurrentIndex(selected_index)

    def draw_charts(self,
                    asset_universe: List[str],
                    implied_returns: pd.Series,
                    selected_chart_type: Optional[str] = ChartTypes.WEIGHTS,
                    *args: pd.Series) -> None:

        # asset_universe = [s.replace(" ", "<br>") for s in asset_universe]  # no word wrap so add line break
        self._set_weights_chart(asset_universe, *args)
        self._set_returns_chart(asset_universe, implied_returns)
        self.select_chart(selected_chart_type)

    def _set_weights_chart(self,
                           asset_universe: List[str],
                           *args: pd.Series) -> None:

        bar_series = QtCharts.QBarSeries()
        y_min = 0
        y_max = 0

        for weights in args:

            weights = weights.reindex(asset_universe)
            y_min = min(weights.min() * 100, y_min)
            y_max = max(weights.max() * 100, y_max)

            bar_set = QtCharts.QBarSet(str(weights.name))
            bar_set.append(weights.mul(100).values.tolist())
            bar_series.append(bar_set)

        # configure basic chart
        chart = QtCharts.QChart()
        chart.setTitle("Black-Litterman Asset Allocation")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        chart.setFont(title_font)
        chart.addSeries(bar_series)

        # configure the x axis
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append([s.replace(" ", "<br>") for s in asset_universe])
        chart.createDefaultAxes()
        chart.setAxisX(axis_x)

        # configure the y axis
        axis_y = QtCharts.QValueAxis()
        self._set_y_axis_limits(y_max, y_min, axis_y)
        axis_y.setLabelFormat("%.0f")
        axis_y.setTitleText("Suggested Allocation (%)")
        chart.setAxisY(axis_y)
        bar_series.attachAxis(axis_y)

        # configure chart legend
        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self._weights_chart_view.setChart(chart)

    def _set_returns_chart(self,
                           asset_universe: List[str],
                           implied_returns: pd.Series) -> None:

        implied_returns = implied_returns.reindex(asset_universe)
        bar_series = QtCharts.QBarSeries()
        bar_set = QtCharts.QBarSet("Returns")
        bar_set.append(implied_returns.mul(100).values.tolist())
        bar_series.append(bar_set)

        # configure basic chart
        chart = QtCharts.QChart()
        chart.setTitle("Market Implied Expected Returns")
        title_font = QtGui.QFont()
        title_font.setBold(True)
        chart.setFont(title_font)
        chart.addSeries(bar_series)

        # configure the x axis
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append([s.replace(" ", "<br>") for s in asset_universe])
        chart.createDefaultAxes()
        chart.setAxisX(axis_x)

        # configure the y axis
        y_min = implied_returns.min() * 100
        y_max = implied_returns.max() * 100
        axis_y = QtCharts.QValueAxis()
        self._set_y_axis_limits(y_max, y_min, axis_y, 2)
        axis_y.setLabelFormat("%.0f")
        axis_y.setTitleText("Expected Return (%pa)")
        chart.setAxisY(axis_y)
        bar_series.attachAxis(axis_y)

        self._returns_chart_view.setChart(chart)

    def _set_y_axis_limits(self,
                           y_max: float,
                           y_min: float,
                           axis_y: QtCharts.QValueAxis,
                           round_to: int = 10) -> None:

        y_max_rounded = self._round_axis_limit(y_max, round_to)
        y_min_rounded = self._round_axis_limit(y_min, round_to)
        intervals = (y_max_rounded - y_min_rounded) // round_to + 1

        axis_y.setMax(y_max_rounded)
        axis_y.setMin(y_min_rounded)
        axis_y.setTickCount(intervals)

    @staticmethod
    def _round_axis_limit(lim: float,
                          round_to: int = 10):

        if lim == 0:
            return 0

        rounded_lim = (math.floor(abs(lim) / round_to) + 1) * round_to
        if lim < 0:
            return -rounded_lim
        else:
            return rounded_lim

    @staticmethod
    def _get_index_for_chart_type(chart_type: str):
        """
        convert the chart type to the index
        of the stacked chart
        """

        if chart_type == ChartTypes.WEIGHTS:
            return 0
        elif chart_type == ChartTypes.RETURNS:
            return 1
        else:
            raise ValueError(f"Unrecognised chart type {chart_type}")



================================================
FILE: black_litterman/ui/view_button.py
================================================
from typing import List
from PySide2 import QtWidgets, QtCore
from black_litterman.domain.views import View
from black_litterman.ui.view_designer_control import ViewDesignerDialog


class ViewButton(QtWidgets.QFrame):

    delete_clicked = QtCore.Signal(QtWidgets.QWidget)
    view_changed = QtCore.Signal()

    def __init__(self,
                 view: View,
                 asset_universe: List[str]):

        super().__init__()
        self._view = view
        self._asset_universe = asset_universe
        self._create_controls()
        self._initialise_controls(view)
        self._add_event_handlers()
        self._add_controls_to_layout()
        self._size_layout()
        self._set_control_style()

    def _create_controls(self):

        self._edit_button = QtWidgets.QPushButton("Edit")
        self._edit_button.setMinimumHeight(30)
        self._edit_button.setMinimumWidth(100)

        self._delete_button = QtWidgets.QPushButton("Delete")
        self._delete_button.setMinimumHeight(30)
        self._delete_button.setMinimumWidth(100)

        self._name_label = QtWidgets.QLabel()
        self._name_label.setMinimumHeight(30)

    def _initialise_controls(self,
                             view: View):

        self._name_label.setText(view.name)

    def _add_event_handlers(self):

        self._edit_button.clicked.connect(self._show_designer)
        self._delete_button.clicked.connect(self._clicked_delete)

    def _add_controls_to_layout(self):

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self._name_label, 0, 0, 1, 2)
        self.layout.addWidget(self._edit_button, 1, 0)
        self.layout.addWidget(self._delete_button, 1, 1)

    def _size_layout(self):

        self.layout.setColumnStretch(0, 5)
        self.layout.setColumnStretch(1, 1)
        self.layout.setColumnStretch(2, 1)

    def _set_control_style(self):

        self.setFrameStyle(QtWidgets.QFrame.StyledPanel)

    def _show_designer(self):
        designer = ViewDesignerDialog(self._view, self._asset_universe)
        result = designer.exec_()
        if result:
            updated_view = designer.get_view()
            if self._view != updated_view:
                self._view = updated_view
                self._name_label.setText(self._view.name)
                self.view_changed.emit()

        designer.deleteLater()

    def _clicked_delete(self):
        self.delete_clicked.emit(self)

    def get_view(self) -> View:

        return self._view


if __name__ == "__main__":

    import sys
    from PySide2 import QtGui
    from black_litterman.domain.views import ViewAllocation

    app = QtWidgets.QApplication([])
    app.setFont(QtGui.QFont("Arial", 10))

    v = View("1", "Bonds outperform equity", 0.5, 2, ViewAllocation("test_1"))
    widget = ViewButton(v, ["asset_1", "asset_2", "asset_3", "asset_4"])
    widget.setWindowTitle("View button")
    widget.resize(30, 100)
    widget.show()

    sys.exit(app.exec_())








================================================
FILE: black_litterman/ui/view_designer_control.py
================================================
from typing import List
from PySide2 import QtWidgets, QtCore
from black_litterman.ui.allocation_controls import AllocationControlRelative, AllocationControlAbsolute
from black_litterman.domain.views import View, ViewAllocation


class ViewDesignerDialog(QtWidgets.QDialog):

    def __init__(self,
                 view: View,
                 asset_universe: List[str]):

        super().__init__()
        self._view = view
        self._asset_universe = asset_universe
        self._create_controls()
        self._initialise_controls(view, asset_universe)
        self._add_event_handlers()
        self._add_controls_to_layout()
        self._size_layout()
        self.setWindowTitle("Edit market view")

    def _create_controls(self) -> None:

        self._name_box = QtWidgets.QLineEdit()
        self._name_box.setFixedHeight(30)

        self._view_type_combo = QtWidgets.QComboBox()
        self._view_type_combo.setFixedHeight(30)

        self._confidence_slider = QtWidgets.QSlider(QtCore.Qt.Orientation.Horizontal)
        self._confidence_slider.setFixedHeight(30)
        self._slider_label = QtWidgets.QLabel()
        self._slider_label.setFixedHeight(30)

        self._outperf_up_down = QtWidgets.QDoubleSpinBox()
        self._outperf_up_down.setFixedHeight(30)

        self._save_button = QtWidgets.QPushButton("Save")
        self._save_button.setMinimumHeight(30)
        self._save_button.setMaximumWidth(100)

        self._exit_button = QtWidgets.QPushButton("Exit")
        self._exit_button.setMinimumHeight(30)
        self._exit_button.setMaximumWidth(100)

        self._allocation_group = QtWidgets.QGroupBox()
        v_box = QtWidgets.QVBoxLayout()
        self._allocation_group.setLayout(v_box)

    def _initialise_controls(self,
                             view: View,
                             asset_universe: List[str]) -> None:

        self._name_box.setText(view.name)

        self._view_type_combo.addItems(ViewAllocation.get_all_view_types())

        self._confidence_slider.setMinimum(0)
        self._confidence_slider.setMaximum(10)
        self._confidence_slider.setTickInterval(1)
        self._confidence_slider.setFixedHeight(30)
        self._confidence_slider.setSliderPosition(int(view.confidence * 10))

        self.slider_label = QtWidgets.QLabel("{:.0%}".format(view.confidence/10))

        self._outperf_up_down.setMinimum(-10)
        self._outperf_up_down.setMaximum(10)
        self._outperf_up_down.setDecimals(1)
        self._outperf_up_down.setSingleStep(0.1)
        self._outperf_up_down.setValue(view.out_performance)

        self._allocation_group.setTitle("View allocation")

        if view.allocation.view_type == ViewAllocation.ABSOLUTE:
            self._allocation_control = AllocationControlAbsolute(view.allocation, asset_universe)
        else:
            self._allocation_control = AllocationControlRelative(view.allocation, asset_universe)
        self._allocation_group.layout().addWidget(self._allocation_control)

    def _add_event_handlers(self):

        self._confidence_slider.valueChanged.connect(self._display_confidence)
        self._view_type_combo.currentTextChanged.connect(self._set_allocation_control)
        self._save_button.clicked.connect(self.on_click_ok)
        self._exit_button.clicked.connect(self.reject)

    def _add_controls_to_layout(self):

        self.layout = QtWidgets.QGridLayout()

        # add main controls
        self.layout.addWidget(self._name_box, 0, 1)
        self.layout.addWidget(self._confidence_slider, 1, 1)
        self.layout.addWidget(self.slider_label, 1, 2)
        self.layout.addWidget(self._view_type_combo, 3, 1)
        self.layout.addWidget(self._outperf_up_down, 2, 1)
        self.layout.addWidget(self._allocation_group, 4, 0, 1, 3)
        self.layout.addWidget(self._save_button, 5, 0)
        self.layout.addWidget(self._exit_button, 5, 1)

        # add control labels
        self.layout.addWidget(QtWidgets.QLabel("View name"), 0, 0)
        self.layout.addWidget(QtWidgets.QLabel("Confidence"), 1, 0)
        self.layout.addWidget(QtWidgets.QLabel("View type"), 3, 0)
        self.layout.addWidget(QtWidgets.QLabel("Return (%pa)"), 2, 0)
        self.setLayout(self.layout)

    def _size_layout(self):
        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 1)
        self.layout.setRowStretch(2, 1)
        self.layout.setRowStretch(3, 10)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 10)
        self.layout.setColumnMinimumWidth(1, 200)
        self.layout.setColumnStretch(2, 1)

    def _display_confidence(self,
                            val):

        self.slider_label.setText("{:.0%}".format(val/10))

    def _set_allocation_control(self,
                                allocation_type):

        self._allocation_group.layout().removeWidget(self._allocation_control)
        self._allocation_control.deleteLater()
        self._allocation_control = None

        if allocation_type == ViewAllocation.ABSOLUTE:
            self._allocation_control = AllocationControlAbsolute(self._view.allocation,
                                                                 self._asset_universe)
        else:
            self._allocation_control = AllocationControlRelative(self._view.allocation,
                                                                 self._asset_universe)

        self._allocation_group.layout().addWidget(self._allocation_control)

    def on_click_ok(self):
        self._view = self._get_view_from_controls()
        self.accept()

    def _get_view_from_controls(self) -> View:

        view_id = self._view.id
        name = self._name_box.text()
        out_performance = self._outperf_up_down.value() / 100
        confidence = self._confidence_slider.value() / 10
        allocation = self._allocation_control.get_allocation()

        view = View(view_id, name, out_performance, confidence, allocation)
        return view

    def get_view(self):
        return self._view




================================================
FILE: black_litterman/ui/view_manager.py
================================================
from typing import List, Dict
from PySide2 import QtWidgets, QtCore
from black_litterman.ui.view_button import ViewButton
from black_litterman.ui.fonts import FontHelper
from black_litterman.domain.views import ViewCollection, View


class ViewManager(QtWidgets.QFrame):

    view_changed = QtCore.Signal()

    def __init__(self, all_views: Dict[str, View], asset_universe: List[str]) -> None:

        super().__init__()
        self._all_views = all_views
        self._asset_universe = asset_universe
        self._create_controls()
        self._add_event_handlers()
        self._add_controls_to_layout()
        self._size_layout()
        self._set_control_style()
        self._view_count = 0

    def _create_controls(self):

        self._views_panel = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignTop)
        self._views_panel.setLayout(layout)
        self._views_panel.setMinimumHeight(300)

        self._add_view_button = QtWidgets.QPushButton("Add new view")
        self._add_view_button.setMinimumHeight(30)

        self._title_label = QtWidgets.QLabel()
        self._title_label.setText("Add market views (max 4)")
        self._title_label.setFont(FontHelper.get_title_font())

    def _add_event_handlers(self):

        self._add_view_button.clicked.connect(self._add_new_view_button)

    def _add_controls_to_layout(self):

        self.layout = QtWidgets.QGridLayout()
        self.setLayout(self.layout)

        self.layout.addWidget(self._title_label, 0, 0)
        self.layout.addWidget(self._views_panel, 1, 0)
        self.layout.addWidget(self._add_view_button, 2, 0)

    def _size_layout(self):

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 9)
        self.layout.setRowStretch(2, 1)

    def _set_control_style(self):

        self.setFrameStyle(QtWidgets.QFrame.StyledPanel | QtWidgets.QFrame.Raised)
        self.setLineWidth(3)

    def _add_new_view_button(self) -> None:

        if self._view_count == 4:
            error_msg = QtWidgets.QMessageBox()
            error_msg.setIcon(QtWidgets.QMessageBox.Critical)
            error_msg.setText("Error")
            error_msg.setInformativeText('Max views reached')
            error_msg.setWindowTitle("Error")
            error_msg.exec_()
        else:
            new_view = View.get_new_view_with_defaults(self._asset_universe[0])
            button = ViewButton(view=new_view, asset_universe=self._asset_universe)
            button.setFixedHeight(75)
            self._views_panel.layout().addWidget(button)
            button.delete_clicked.connect(self._delete_button)
            button.view_changed.connect(self._raise_view_changed)
            self._view_count += 1
            self.view_changed.emit()

    def _delete_button(self,
                       button):
        button.setParent(None)
        self.view_changed.emit()
        self._view_count -= 1

    def _raise_view_changed(self):
        self.view_changed.emit()

    def get_all_views(self) -> ViewCollection:

        all_views = ViewCollection()

        for child_control in self._views_panel.children():
            if isinstance(child_control, ViewButton):
                view = child_control.get_view()
                all_views.add_view(view)

        return all_views




================================================
FILE: tests/test_domain/test_engine.py
================================================
import unittest
import pandas as pd
from unittest import mock
from black_litterman.domain.engine import BLEngine, CalculationSettings
from black_litterman.domain.views import View, ViewAllocation, ViewCollection


class TestEngine(unittest.TestCase):

    @staticmethod
    def _get_market_data():
        asset_universe = ["asset_1", "asset_2", "asset_3"]
        market_cov = pd.DataFrame([[0.18, -0.04, 0], [-0.04, 0.05, 0.07], [0, 0.07, 0.11]],
                                  index=asset_universe, columns=asset_universe)
        market_weights = pd.Series([0.3, 0.5, 0.2], index=asset_universe)

        return market_cov, market_weights

    @staticmethod
    def _get_bl_engine():
        calc_settings = CalculationSettings(1, 3, None, None, ["asset_1", "asset_2", "asset_3"])
        mock_data_reader = mock.MagicMock()
        engine = BLEngine(mock_data_reader, calc_settings)
        return engine

    def test_get_bl_weights_absolute_view(self):
        # arrange
        market_cov, market_weights = self._get_market_data()
        engine = self._get_bl_engine()
        view_matrix = pd.Series([1, 0, 0], index=market_cov.index, name="view_1").to_frame().T
        view_cov = pd.DataFrame([[0.05]], index=["view_1"], columns=["view_1"])
        view_outperf = pd.Series([0.2], index=["view_1"])

        # act
        result = engine._get_weights(market_weights, market_cov, view_matrix, view_cov,
                                     view_outperf)

        # assert
        expected_result = pd.Series([0.442028986, 0.5, 0.2], index=market_cov.index)
        pd.testing.assert_series_equal(expected_result, result)

    def test_get_bl_weights_relative_view(self):
        # arrange
        market_cov, market_weights = self._get_market_data()
        engine = self._get_bl_engine()
        view_matrix = pd.Series([0, -1, 1], index=market_cov.index, name="view_1").to_frame().T
        view_cov = pd.DataFrame([0.1], index=["view_1"], columns=["view_1"])
        view_outperf = pd.Series([0.06], index=["view_1"])

        # act
        result = engine._get_weights(market_weights, market_cov, view_matrix, view_cov,
                                       view_outperf)

        # assert
        expected_result = pd.Series([0.3, 0.5833333, 0.1166667], index=market_cov.index)
        pd.testing.assert_series_equal(expected_result, result)

    def test_get_bl_weights_multiple_views(self):
        # arrange
        market_cov, market_weights = self._get_market_data()
        engine = self._get_bl_engine()
        view_matrix = pd.DataFrame([[0, -1, 1], [1, 0, 0], [-1, 0, 1]], index=["view_1", "view_2", "view_3"],
                                   columns=market_cov.index)
        view_cov = pd.DataFrame([[0.1, 0, 0], [0, 0.05, 0], [0, 0, 0.04]], index=["view_1", "view_2", "view_3"],
                                columns=["view_1", "view_2", "view_3"])
        view_outperf = pd.Series([0.05, 0.09, 0.08], index=["view_1", "view_2", "view_3"])

        # act
        result = engine._get_weights(market_weights, market_cov, view_matrix, view_cov,
                                       view_outperf)

        # assert
        expected_result = pd.Series([0.2982666, 0.6179881, 0.1043762], index=market_cov.index)
        pd.testing.assert_series_equal(expected_result, result)

    def test_get_sum_squares(self):
        # arrange
        series_1 = pd.Series([0.5, 0.25, 0.75, 0.3])
        series_2 = pd.Series([0.2, 0.3, 0.75, 0.4])

        # act
        result = BLEngine._get_sum_squares_error(series_1, series_2)

        # assert
        self.assertAlmostEqual(0.1025, result)

    def test_get_target_weights_relative_view(self):
        # arrange
        test_view = View("1", "test_view", 0.08, 0.5, ViewAllocation("asset_3", "asset_2"))
        market_cov, market_weights = self._get_market_data()
        engine = self._get_bl_engine()
        view_matrix = test_view.get_view_data_frame(["asset_1", "asset_2", "asset_3"])
        view_out_performance = pd.Series([0.08], index=["1"])

        # act
        result = engine._get_view_target_weights(test_view, market_weights, market_cov,
                                                   view_matrix, view_out_performance)

        # assert
        expected_result = pd.Series([0.3, 0.58333333, 0.11666667], index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_series_equal(expected_result, result)

    def test_get_target_weights_absolute_view(self):
        # arrange
        test_view = View("1", "test_view", 0.13, 0.8, ViewAllocation("asset_1", None))
        market_cov, market_weights = self._get_market_data()
        engine = self._get_bl_engine()
        view_matrix = test_view.get_view_data_frame(["asset_1", "asset_2", "asset_3"])
        view_out_performance = pd.Series([0.13], index=["1"])

        # act
        result = engine._get_view_target_weights(test_view, market_weights, market_cov,
                                                   view_matrix, view_out_performance)

        # assert
        expected_result = pd.Series([0.3414814815, 0.5, 0.2], index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_series_equal(expected_result, result)

    def test_confidence_to_variance_absolute_view(self):
        # arrange
        view = View("test_view", "test_view", 0.13, 0.5, ViewAllocation("asset_1"))
        market_cov, market_weights = self._get_market_data()
        bl_engine = self._get_bl_engine()

        # act
        result = bl_engine._confidence_to_variance(view, market_weights, market_cov)

        # assert
        self.assertAlmostEqual(0.18, result, delta=1e-4)

    def test_confidence_to_variance_relative_view(self):
        # arrange
        view = View("test_view", "test_view", 0.06, 0.3, ViewAllocation("asset_3", "asset_2"))
        market_cov, market_weights = self._get_market_data()
        bl_engine = self._get_bl_engine()

        # act
        result = bl_engine._confidence_to_variance(view, market_weights, market_cov)

        # assert
        self.assertAlmostEqual(0.04667, result, delta=1e-4)

    def test_get_view_covariances_from_confidences(self):
        # arrange
        view_collection = ViewCollection()
        view_collection.add_view(View("view_1", "view_1", 0.14, 0.6, ViewAllocation("asset_1")))
        view_collection.add_view(View("view_2", "view_2", 0.06, 0.3, ViewAllocation("asset_3", "asset_2")))

        engine = self._get_bl_engine()
        mock_conf_to_var = mock.MagicMock()
        mock_conf_to_var.side_effect = [0.1, 0.05]
        engine._confidence_to_variance = mock_conf_to_var

        market_cov, market_weight = self._get_market_data()

        # act
        result = engine.get_view_covariances_from_confidences(market_weight, market_cov, view_collection)

        # assert
        expected_result = pd.DataFrame([[0.1, 0], [0, 0.05]], index=["view_1", "view_2"], columns=["view_1", "view_2"])
        pd.testing.assert_frame_equal(expected_result, result)












================================================
FILE: tests/test_domain/test_views.py
================================================
import unittest
import pandas as pd
from black_litterman.domain.views import ViewAllocation, ViewCollection, View


class TestViews(unittest.TestCase):

    @staticmethod
    def _get_view_collection(collection_type: str):

        view_allocation_1 = ViewAllocation("asset_2")
        view_1 = View("1", "view_1", 0.06, 0.5, view_allocation_1)
        view_allocation_2 = ViewAllocation("asset_1", "asset_3")
        view_2 = View("2", "view_2", 0.02, 0.9, view_allocation_2)
        view_allocation_3 = ViewAllocation("asset_3", "asset_2")
        view_3 = View("3", "view_3", 0.08, 0.2, view_allocation_3)

        view_collection = ViewCollection()
        if collection_type == "none":
            return view_collection
        elif collection_type == "absolute":
            view_collection.add_view(view_1)
            return view_collection
        elif collection_type == "relative":
            view_collection.add_view(view_2)
            view_collection.add_view(view_3)
            return view_collection
        else:
            view_collection.add_view(view_1)
            view_collection.add_view(view_2)
            view_collection.add_view(view_3)
            return view_collection

    def test_get_view_matrix_no_views(self):
        # arrange
        view_collection = self._get_view_collection("none")
        asset_universe = ["asset_1", "asset_2", "asset_3", "asset_4"]

        # act
        result = view_collection.get_view_matrix(asset_universe)

        # assert
        expected_result = pd.DataFrame()
        pd.testing.assert_frame_equal(expected_result, result)

    def test_get_view_matrix_absolute_view(self):
        # arrange
        view_collection = self._get_view_collection("absolute")
        asset_universe = ["asset_1", "asset_2", "asset_3", "asset_4"]

        # act
        result = view_collection.get_view_matrix(asset_universe)

        # assert
        expected_result = pd.Series([0, 1, 0, 0], index=asset_universe, name="1").to_frame().T
        pd.testing.assert_frame_equal(expected_result, result)

    def test_get_view_matrix_relative(self):
        # arrange
        view_collection = self._get_view_collection("relative")
        asset_universe = ["asset_1", "asset_2", "asset_3", "asset_4"]

        # act
        result = view_collection.get_view_matrix(asset_universe)

        # assert
        expected_result = pd.DataFrame([[1, 0, -1, 0], [0, -1, 1, 0]], index=["2", "3"],
                                       columns=asset_universe)
        pd.testing.assert_frame_equal(expected_result, result)

    def test_get_view_matrix_all_view_types(self):
        # arrange
        view_collection = self._get_view_collection("")
        asset_universe = ["asset_1", "asset_2", "asset_3", "asset_4"]

        # act
        result = view_collection.get_view_matrix(asset_universe)

        # assert
        expected_result = pd.DataFrame([[0, 1, 0, 0], [1, 0, -1, 0], [0, -1, 1, 0]], index=["1", "2", "3"],
                                       columns=asset_universe)
        pd.testing.assert_frame_equal(expected_result, result)

    def test_get_out_performance(self):
        # arrange
        view_collection = self._get_view_collection("")

        # act
        result = view_collection.get_view_out_performances()

        # assert
        expected_result = pd.Series({"1": 0.06, "2": 0.02, "3": 0.08})
        pd.testing.assert_series_equal(expected_result, result)

    def test_get_view_cov_matrix(self):
        # arrange
        view_collection = self._get_view_collection("")

        # act
        result = view_collection.get_view_confidence_matrix()

        # assert
        expected_result = pd.DataFrame([[0.5, 0, 0], [0, 0.9, 0], [0, 0, 0.2]],
                                       index=["1", "2", "3"], columns=["1", "2", "3"])
        pd.testing.assert_frame_equal(expected_result, result, check_dtype=False)





================================================
FILE: tests/test_market_data/test_engine.py
================================================
import unittest
import pandas as pd
from datetime import datetime
from black_litterman.market_data.engine import MarketDataEngine


class TestMarketDataEngine(unittest.TestCase):

    @staticmethod
    def _get_market_data_engine() -> MarketDataEngine:

        dates = pd.date_range(start=datetime(2020, 3, 1), end=datetime(2020, 3, 10), freq="B")
        price_data = pd.DataFrame({"asset_1": [100, 101, 102, 100, 98, 99, 100],
                                   "asset_2": [95, 94, 97, 93, 95, 97, 99],
                                   "asset_3": [20, 20.5, 20.5, 20.5, 19.5, 19, 18]},
                                  index=dates)

        market_cap_data = pd.DataFrame({"asset_1": [1000000, 1000000, 1000000, 1000000, 1020000, 1020000, 1020000],
                                        "asset_2": [500000, 500000, 500000, 400000, 400000, 250000, 250000],
                                        "asset_3": [500000, 500000, 400000, 200000, 400000, 500000, 500000]},
                                       index=dates)

        engine = MarketDataEngine(price_data, market_cap_data)
        return engine

    def test_get_covariance_all_dates(self):
        # arrange
        engine = self._get_market_data_engine()
        start_date = "2020-03-01"
        end_date = "2020-03-10"

        # act
        result = engine.get_annualised_cov_matrix(start_date, end_date)

        # assert
        expected_result = {"asset_1": [0.05943, 0.05040, 0.02213],
                           "asset_2": [0.05040, 0.19239, -0.11001],
                           "asset_3": [0.02213, -0.11001, 0.23481]}
        expected_result = pd.DataFrame(expected_result, index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_frame_equal(expected_result, result, check_less_precise=True)

    def test_get_covariance_different_end_date(self):
        # arrange
        engine = self._get_market_data_engine()
        start_date = "2020-03-01"
        end_date = "2020-03-05"

        # act
        result = engine.get_annualised_cov_matrix(start_date, end_date)

        # assert
        expected_result = {"asset_1": [0.07281, 0.12765, 0.03094],
                           "asset_2": [0.12765, 0.33732, -0.01222],
                           "asset_3": [0.03094, -0.01222, 0.05208]}
        expected_result = pd.DataFrame(expected_result, index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_frame_equal(expected_result, result, check_less_precise=True)

    def test_get_covariance_different_start_date(self):
        # arrange
        engine = self._get_market_data_engine()
        start_date = "2020-03-05"
        end_date = "2020-03-10"

        # act
        result = engine.get_annualised_cov_matrix(start_date, end_date)

        # assert
        expected_result = pd.DataFrame({"asset_1": [0.07479, 0.07562, -0.03590],
                                        "asset_2": [0.07562, 0.24258, -0.16476],
                                        "asset_3": [-0.03590, -0.16476, 0.14762]},
                                       index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_frame_equal(expected_result, result, check_less_precise=True)

    def test_get_market_weights(self):
        # arrange
        engine = self._get_market_data_engine()
        selected_date = "2020-03-05"

        # act
        result = engine.get_market_weights(selected_date)

        # assert
        expected_result = pd.Series([0.625, 0.25, 0.125], index=["asset_1", "asset_2", "asset_3"])
        pd.testing.assert_series_equal(expected_result, result, check_names=False)


