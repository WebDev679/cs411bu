from typing import Optional

from wildlife_tracker.habitat_management.habitat import Habitat


class MigrationPath:

    def __init__(self, 
               destination: Habitat,
               path_id: int,
               species: str,
               start_location: Habitat,
               start_date: str,
               duration: Optional[int] = None,
               health_status: Optional[str] = None,) -> None:
        pass

    def get_migration_path_details(self) -> dict:
        pass

    def update_migration_path_details(self, **kwargs) -> None:
        pass

