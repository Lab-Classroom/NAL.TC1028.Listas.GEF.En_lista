import pytest
import src.exercise

def test_exercise():
    input_values = ["Tom","Emma","Alex","Mary","","Mary","Tom","Emma","Alex","Mary","","Logan"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["","","","","","Search for? ","Mary was found!",\
                        "","","","","","Search for? ","Logan was not found!"]
