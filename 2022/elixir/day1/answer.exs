file = Path.expand('2022/input/day1/input') |> Path.absname()
input = File.read!(file)

data =
  String.split(input, "\n\n", trim: true)
  |> Enum.map(fn line ->
    String.split(line, "\n", trim: true)
    |> Enum.map(&String.to_integer/1)
  end)

answer1 = data |> Enum.map(&Enum.sum(&1)) |> Enum.max()
answer2 = data |> Enum.map(&Enum.sum(&1)) |> Enum.sort(:desc) |> Enum.take(3) |> Enum.sum()

IO.inspect(answer1)
IO.inspect(answer2)
