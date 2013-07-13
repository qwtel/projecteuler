import Time.time
import scala.math._

object ProjEul6 {
  def main(args: Array[String]) = {
    val res = time {
      abs(
        pow((1 to 100).sum, 2) -
          (1 to 100).map(x => pow(x, 2)).sum
      )
    }
    println(res.toInt)
  }
}
