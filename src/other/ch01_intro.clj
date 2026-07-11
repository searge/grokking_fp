;; Imperative and declarative programming
;; Imperative programming: write code that does what you want
;; Declarative programming: write code that describes what you want

(ns ch01-intro)

(defn calculate-score
  "Calculate the score of a word by counting its characters imperatively."
  [word]
  (let [score (atom 0)]
    (doseq [_ word]
      (swap! score inc))
    @score))

(defn word-score
  "Calculate the score of a word declaratively using built-in count."
  [word]
  (count word))

(defn calculate-score2
  "Calculate the score of a word by counting non-'a' characters imperatively."
  [word]
  (let [score (atom 0)]
    (doseq [char word]
      (when (not= char \a)
        (swap! score inc)))
    @score))

(defn word-score2
  "Calculate the score of a word declaratively by subtracting 'a' count."
  [word]
  (- (count word)
     (count (filter #(= % \a) word))))

(defn string-without-char
  "Remove all occurrences of a character from a string."
  [word char]
  (apply str (remove #(= % char) word)))

(defn word-score3
  "Calculate word score by removing 'a' characters and counting length."
  [word]
  (count (string-without-char word \a)))

(defn -main
  "Run the examples."
  []
  (println (str "calculate-score: " (calculate-score "imperative")))
  (println (str "word-score: " (word-score "declarative")))

  (try
    (assert (= (calculate-score "imperative") 10))
    (assert (= (word-score "declarative") 11))
    (println "First assertion passed")
    (catch AssertionError _
      (println "First assertion failed")))

  (println (str "calculate-score2: " (calculate-score2 "imperative")))
  (println (str "word-score2: " (word-score2 "declarative")))
  (println (str "word-score3: " (word-score3 "declarative")))

  (try
    (assert (= (calculate-score2 "imperative") 9))
    (assert (= (word-score2 "declarative") 9))
    (assert (= (word-score3 "declarative") 9))
    (println "Second assertion passed")
    (catch AssertionError _
      (println "Second assertion failed"))))

(-main)
