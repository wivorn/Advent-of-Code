file = Path.expand('2022/input/day3/input') |> Path.absname()
input = File.read!(file)

data = String.split(input, "\n", trim: true)

defmodule Rucksack do
  def find_duplicate(line) do
    half_index = div(String.length(line), 2) - 1
    a = MapSet.new(String.graphemes(String.slice(line, 0..half_index)))
    b = MapSet.new(String.graphemes(String.slice(line, (half_index + 1)..-1)))
    hd(MapSet.to_list(MapSet.intersection(a, b)))
  end

  def find_badge(group) do
    a = MapSet.new(String.graphemes(Enum.at(group, 0)))
    b = MapSet.new(String.graphemes(Enum.at(group, 1)))
    c = MapSet.new(String.graphemes(Enum.at(group, 2)))
    hd(MapSet.to_list(MapSet.intersection(MapSet.intersection(a, b), c)))
  end

  def get_priority(char) do
    val = :binary.first(char)
    if val > 96, do: val - 96, else: val - 38
  end
end

answer1 =
  data
  |> Enum.map(&Rucksack.find_duplicate(&1))
  |> Enum.map(&Rucksack.get_priority(&1))
  |> Enum.sum()

answer2 =
  data
  |> Enum.chunk_every(3)
  |> Enum.map(&Rucksack.find_badge(&1))
  |> Enum.map(&Rucksack.get_priority(&1))
  |> Enum.sum()

IO.inspect(answer1)
IO.inspect(answer2)
