import Time.time
import scala.math._

object ProjEul9 {
  def main(args: Array[String]) = {
    val x = time(find)
    println(x)
  }

  def find: Int = {
    (for {
      c <- 1 to 1000
      b <- 1 to c
      a <- 1 to b
      if a + b + c == 1000
      if pow(a, 2) + pow(b, 2) == pow(c, 2)
    } yield a*b*c).toList(0)
  }

  /*
   * From the Project Euler forum
   */
  def findBetter: Int = {
    def findTriplet(n: Int): (Double, Double, Double) = {
      val delta = pow(n, 2) + 2*1000
      val m1 = (-n + sqrt(delta)) / 2
      val m2 = (-n - sqrt(delta)) / 2
      val m =
        if (m1.isValidInt && m1 > n) m1
        else if (m2.isValidInt && m2 > n) m2
        else 0
      if (m != 0)
        (2*m*n, pow(m, 2) - pow(n, 2), pow(m, 2) + pow(n, 2))
      else findTriplet(n + 1)
    }

    val (a, b, c) = findTriplet(1)
    (a * b * c).toInt
  }
}
