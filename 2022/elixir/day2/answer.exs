file = Path.expand('2022/input/day2/input') |> Path.absname()
input = File.read!(file)

data = String.split(input, "\n", trim: true)

defmodule RPS do
  @score_map %{X: 1, Y: 2, Z: 3}
  @score_map2 %{X: 0, Y: 3, Z: 6}

  def get_score(round) do
    [a, b] = String.split(round) |> Enum.map(&String.to_atom/1)

    case [a, b] do
      [:A, :Z] -> 0 + @score_map[b]
      [:B, :X] -> 0 + @score_map[b]
      [:C, :Y] -> 0 + @score_map[b]
      [:A, :X] -> 3 + @score_map[b]
      [:B, :Y] -> 3 + @score_map[b]
      [:C, :Z] -> 3 + @score_map[b]
      [:A, :Y] -> 6 + @score_map[b]
      [:B, :Z] -> 6 + @score_map[b]
      [:C, :X] -> 6 + @score_map[b]
    end
  end

  def get_score2(round) do
    [a, b] = String.split(round) |> Enum.map(&String.to_atom/1)

    case [a, b] do
      [:A, :X] -> 3 + @score_map2[b]
      [:B, :X] -> 1 + @score_map2[b]
      [:C, :X] -> 2 + @score_map2[b]
      [:A, :Y] -> 1 + @score_map2[b]
      [:B, :Y] -> 2 + @score_map2[b]
      [:C, :Y] -> 3 + @score_map2[b]
      [:A, :Z] -> 2 + @score_map2[b]
      [:B, :Z] -> 3 + @score_map2[b]
      [:C, :Z] -> 1 + @score_map2[b]
    end
  end
end

answer1 = data |> Enum.map(&RPS.get_score(&1)) |> Enum.sum()
answer2 = data |> Enum.map(&RPS.get_score2(&1)) |> Enum.sum()

IO.inspect(answer1)
IO.inspect(answer2)
