file = Path.expand('2022/input/day5/example') |> Path.absname()
input = File.read!(file)

[state, instruction] =
  input |> String.split("\n\n", trim: true) |> Enum.map(&String.split(&1, "\n", trim: true))

defmodule Day5 do
  def parse_state(state) do
    state
    |> Enum.map(fn line ->
      String.codepoints(line)
      |> Enum.chunk_every(4)
      |> Enum.map(&Enum.join/1)
      |> Enum.map(&String.trim/1)
    end)
    |> Enum.reverse()
    |> build_stack()
  end

  def build_stack(state) do
    [head | lines] = state

    lines
    |> Enum.reduce([], fn (line, acc) ->
      line
      |> Enum.with_index()
      |> Enum.each(fn {c, i} ->
        if Enum.at(acc, i) do
          acc =
        else

        end
      end)
      end
    end)
  end
end

Day5.parse_state(state)
