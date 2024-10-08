from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class Migration:

    def __init__(self, 
               migration_id: int,
               current_date: str,
               current_location: str,
               migration_path: MigrationPath,
               species: str,
               status: str = "Scheduled") -> None:
        pass

    def get_migration_details(self) -> dict[str, Any]:
        pass

    def update_migration_details(self, **kwargs: Any) -> None:
        pass

 

