def find(n: Int): Int = {
  if ((1 to 20).forall(d => n%d == 0)) n
  else find(n + 1)
}

WithTime.time {
  val res = find(1)
  println(res)
}
