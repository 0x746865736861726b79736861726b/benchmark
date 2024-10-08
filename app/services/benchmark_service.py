from typing import Dict
from app.repo.benchmark_repo import BenchmarkRepository


class BenchmarkService:
    def __init__(self, repository: BenchmarkRepository):
        self.repository = repository

    async def calculate_average_statistic(self, results) -> Dict:
        """
        Calculate average statistics from a given list of results.

        Args:
            results (List[Benchmark]): A list of benchmark results.

        Returns:
            Dict: A dictionary with average statistics. The dictionary contains the following keys:
                - `avarage_token_count`: The average number of tokens in the results.
                - `avarage_time_to_first_token`: The average time to generate the first token in the results.
                - `avarage_time_per_token_output`: The average time per token output in the results.
                - `avarage_total_generation_time`: The average total generation time in the results.
        """
        total_results = len(results)
        if total_results == 0:
            return {}

        avarage_stats = {
            "avarage_token_count": sum(result.token_count for result in results)
            / total_results,
            "avarage_time_to_first_token": sum(
                result.time_to_first_token for result in results
            )
            / total_results,
            "avarage_time_per_token_output": sum(
                result.time_per_output_token for result in results
            )
            / total_results,
            "avarage_total_generation_time": sum(
                result.total_generation_time for result in results
            )
            / total_results,
        }

        return avarage_stats

    async def get_average_statistics(self) -> Dict:
        results = await self.repository.get_all_results()
        return await self.calculate_average_statistic(results)

    async def get_average_statistics_between(
        self, start_time: str, end_time: str
    ) -> Dict:
        results = await self.repository.get_average_statistics_between(
            start_time, end_time
        )
        return await self.calculate_average_statistic(results)
