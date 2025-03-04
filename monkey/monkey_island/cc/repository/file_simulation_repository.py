import io

from monkey_island.cc import repository
from monkey_island.cc.models import IslandMode, Simulation
from monkey_island.cc.repository import IFileRepository, ISimulationRepository, RetrievalError

SIMULATION_STATE_FILE_NAME = "simulation_state.json"


class FileSimulationRepository(ISimulationRepository):
    def __init__(self, file_repository: IFileRepository):
        self._file_repository = file_repository

    def get_simulation(self) -> Simulation:
        try:
            with self._file_repository.open_file(SIMULATION_STATE_FILE_NAME) as f:
                simulation_json = f.read().decode()

            return Simulation.parse_raw(simulation_json)
        except repository.FileNotFoundError:
            return Simulation()
        except Exception as err:
            raise RetrievalError(f"Error retrieving the simulation state: {err}")

    def save_simulation(self, simulation: Simulation):
        simulation_json = simulation.json()

        self._file_repository.save_file(
            SIMULATION_STATE_FILE_NAME, io.BytesIO(simulation_json.encode())
        )

    def get_mode(self) -> IslandMode:
        return self.get_simulation().mode

    def set_mode(self, mode: IslandMode):
        self.save_simulation(Simulation(mode=mode))
