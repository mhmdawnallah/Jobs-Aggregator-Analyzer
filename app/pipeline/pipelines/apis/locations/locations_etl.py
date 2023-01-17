from typing import AsyncGenerator, Optional
import pandas as pd
import json
from common.etls_common import DataPipeline, Extractor, Transformer, Loader
from extractors.scrappers.indeed.countries_scrapper import IndeedCountriesScrapper
from pipeline.models.country_model import CountryDim
from pipeline.utilities.utils import Utils
from extractors.apis.fortune_companies.fortune_companies_api_extractor import FortuneCompaniesAPIExtractor 
from pipeline.transformers.scrappers.indeed.countries_transformer import IndeedCountriesTransformer
from app.utilities.decorators import timer
from pipeline.transformers.apis.fortune_companies_transformer import FortuneCompaniesAPITransformer
from loguru import logger

class LocationsETL(Transformer, Loader, DataPipeline):
    """Indeed ETL class"""
    def __init__(self, locations_df: pd.DataFrame, silver_storage_path: str, gold_storage_path: str):
        self.locations_df = locations_df
        self.silver_storage_path = silver_storage_path
        self.gold_storage_path = gold_storage_path

    def transform(self) -> pd.DataFrame:
        """Transform data"""
        fortune_companies_df: pd.DataFrame = FortuneCompaniesAPITransformer.transform(fortune_companies)
        fortune_companies_transformed_df: pd.DataFrame = FortuneCompaniesAPITransformer.transform_df(fortune_companies_df)
        return fortune_companies_transformed_df

    def load(self, fortune_companies_df: pd.DataFrame) -> bool:
        """Load data into the CSV"""
        fortune_companies_df.to_csv(self.staging_storage_path)
        return True
    
    @timer
    async def run(self):
        """Run the ETL"""
        fortune_companies: dict = await self.extract()
        fortune_companies_transformed_df: pd.DataFrame = self.transform(fortune_companies)
        is_loaded: bool = self.load(fortune_companies_transformed_df)
        return is_loaded
