import pytest
from agbenchmark.challenges.define_task_types import ChallengeData
from agbenchmark.tests.basic_abilities.BasicChallenge import BasicChallenge
import os

data = ChallengeData.deserialize(
    os.path.join(os.path.dirname(__file__), "w_file_data.json")
)


class TestWriteFile(BasicChallenge):
    """Testing if LLM can write to a file"""

    @pytest.mark.parametrize(
        "server_response",
        [(data.task, data.mock_func)],
        indirect=True,
    )
    @pytest.mark.parametrize(
        "regression_data",
        [data],
        indirect=True,
    )
    @pytest.mark.depends(name="test_write_file")
    def test_write_file(self, workspace):
        files_contents = self.open_files(workspace, data.ground.files)

        scores = []
        for file_content in files_contents:
            score = self.scoring(file_content, data.ground)
            print("Your score is:", score)
            scores.append(score)

        assert 1 in scores
