import pytest
from etl.scrappers.indeed_scrapper import IndeedScrapper
from etl.scrappers.data_stack_jobs_scraper import DataStackJobsScraper
from pipeline.utilities.utils import Utils
from etl.utilities.job_specifications import OrSpecification,ProgrammingLanguagesSpecification,IngestTechSpecification, BachelorComputerScienceSpecification
from apis.lightcast.job_skills_apis import JobSkillsAPI

@pytest.fixture(scope="session")
def etl_configs() -> dict:
    """Fixture for configs"""
    configs: dict = Utils.get_configs("app/etl/settings/pipeline_configs.yaml")
    return configs


@pytest.fixture(scope="session")
def job_skills(etl_configs: dict) -> str:
    """Fixture for job skills"""
    skills_api = JobSkillsAPI(etl_configs["data_sources"]["lightcast_skills"])
    skills: str = skills_api.get_latest_job_skills()
    return skills

@pytest.fixture(scope="session")
def indeed_scrapper(etl_configs: dict, job_skills: str) -> IndeedScrapper:
    """Fixture for Indeed scrapper"""
    return IndeedScrapper(etl_configs["data_sources"]["indeed"],job_skills)
