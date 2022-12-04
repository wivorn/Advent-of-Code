file = Path.expand('2022/input/day4/input') |> Path.absname()
input = File.read!(file)

data = String.split(input, "\n", trim: true)

defmodule Job do
  def full_overlap(line) do
    [a, b] =
      String.split(line, ",", trim: true)
      |> Enum.map(&String.split(&1, "-"))

    [aMin, aMax] = a |> Enum.map(&String.to_integer/1)
    [bMin, bMax] = b |> Enum.map(&String.to_integer/1)

    cond do
      aMin <= bMin and aMax >= bMax -> 1
      bMin <= aMin and bMax >= aMax -> 1
      true -> 0
    end
  end

  def overlap(line) do
    [a, b] =
      String.split(line, ",", trim: true)
      |> Enum.map(&String.split(&1, "-"))

    [aMin, aMax] = a |> Enum.map(&String.to_integer/1)
    [bMin, bMax] = b |> Enum.map(&String.to_integer/1)

    cond do
      aMin >= bMin and aMin <= bMax -> 1
      bMin >= aMin and bMin <= aMax -> 1
      true -> 0
    end
  end
end

answer1 = data |> Enum.map(&Job.full_overlap/1) |> Enum.sum()
answer2 = data |> Enum.map(&Job.overlap/1) |> Enum.sum()

IO.inspect(answer1)
IO.inspect(answer2)
