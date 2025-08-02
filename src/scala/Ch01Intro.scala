// Imperative and declarative programming
// Imperative programming: write code that does what you want
// Declarative programming: write code that tells you what to do

object Ch01Intro:

  /** Calculate the score of a word by counting its characters imperatively.
   *
   * @param word The input word to score.
   * @return The number of characters in the word.
   */
  def calculateScore(word: String): Int =
    var score: Int = 0
    for _ <- word do
      score += 1
    score

  /** Calculate the score of a word declaratively using built-in length.
   *
   * @param word The input word to score.
   * @return The number of characters in the word.
   */
  def wordScore(word: String): Int = word.length

  /** Calculate the score of a word by counting non-'a' characters imperatively.
   *
   * @param word The input word to score.
   * @return The number of characters in the word excluding 'a'.
   */
  def calculateScore2(word: String): Int =
    var score: Int = 0
    for char <- word do
      if char != 'a' then
        score += 1
    score

  /** Calculate the score of a word declaratively by subtracting 'a' count.
   *
   * @param word The input word to score.
   * @return The number of characters in the word excluding 'a'.
   */
  def wordScore2(word: String): Int =
    word.length - word.count(_ == 'a')

  /** Remove all occurrences of a character from a string.
   *
   * @param word The input string.
   * @param char The character to remove.
   * @return A new string with all occurrences of char removed.
   */
  def stringWithoutChar(word: String, char: Char): String =
    word.filter(_ != char)

  /** Calculate word score by removing 'a' characters and counting length.
   *
   * @param word The input word to score.
   * @return The number of characters in the word excluding 'a'.
   */
  def wordScore3(word: String): Int =
    stringWithoutChar(word, 'a').length

  // Main method to run the examples
  @main def runExamples(): Unit =
    println(s"calculateScore: ${calculateScore("imperative")}")
    println(s"wordScore: ${wordScore("declarative")}")

    // Assertions for first set
    try
      assert(calculateScore("imperative") == 10)
      assert(wordScore("declarative") == 11)
      println("First assertion passed")
    catch
      case _: AssertionError => println("First assertion failed")

    // Coffee Break exercise results
    println(s"calculateScore2: ${calculateScore2("imperative")}")
    println(s"wordScore2: ${wordScore2("declarative")}")
    println(s"wordScore3: ${wordScore3("declarative")}")

    // Assertions for second set
    try
      assert(calculateScore2("imperative") == 9)
      assert(wordScore2("declarative") == 9)
      assert(wordScore3("declarative") == 9)
      println("Second assertion passed")
    catch
      case _: AssertionError => println("Second assertion failed")
