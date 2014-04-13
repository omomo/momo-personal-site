Title: [ML Notes] - Naive Bayes
Date: 2014-04-08 23:00
Tags: data science, machine learning, notes
Slug: naive-bayes
Author: Momo Ong
Excerpt: The Naive Bayes Classifier

### The Classification Problem
Let $C$ be a class, and $F_{i1}, F_{i2}, \ldots, F_{in}$ be the $n$ features in the $i$th instance. Given observed features, the probability that the $i$th instance belongs to class $C$ is simply

$$ P(C|F_{i1}, F_{i2}, \ldots, F_{in})$$

Thus, the classification problem seeks to determine the following

$$\underset{c} {\mathrm{argmax}} P(C|F_{i1}, F_{i2}, \ldots, F_{in})$$

---

### The Naive Bayes Classifier
Using Bayes' Theorem, we can know that the above conditional probability can be written as

$$ P(C|F_{i1}, F_{i2}, \ldots, F_{in}) = \frac{P(C)P(F_{i1}, F_{i2}, \ldots, F_{in}|C)}{P(F_{i1}, F_{i2}, \ldots, F_{in})}$$

Now for a few definitions to better understand the terms in the above equation:

1. $P(C)$ is the _a priori_, or _prior_ probability of the class $C$. This is the probability that an instance belongs to class $C$, _prior_ to knowing anything about the instance's features. Suppose there were 2 blue balls and 5 red balls. The _a priori_ probability of blue balls and red balls would be $2/7$ and $5/7$ respectively.
2. $P(C|F_{i1}, F_{i2}, \ldots, F_{in})$ is termed the _a posteriori_ probability of class $C$. This is the probability that an instance belongs to class $C$, _given_ knowledge of the instance's features.
3. $P(F_{i1}, F_{i2}, \ldots, F_{in}|C)$ can be seen as the _likelihood_ function of $C$.

Now, we assume the independence of all features to each other given the class $C$. This is the naive part of the classifier that gives it its name and allows us to rewrite the above Bayesian equation as

$$ P(C|F_{i1}, F_{i2}, \ldots, F_{in}) = \frac{P(C) P(F_{i1}|C) P(F_{i2}|C) \ldots P(F_{in}|C)}{P(F_{i1}, F_{i2}, \ldots, F_{in})} $$

Since we are not interested in the absolute value of $P(C|F_{i1}, F_{i2}, \ldots, F_{in})$, the denominator of the above equation does not matter, and the Naive Bayes classifier algorithm can be understood to calculate

$$ P(C) \underset{c} {\mathrm{argmax}} \prod_i P(F_i|C) $$

---

Sources

1. [Wikipedia](http://en.wikipedia.org/wiki/Naive_Bayes_classifier)
2. [Ourmine NaiveBayes Classifiers 101](https://code.google.com/p/ourmine/wiki/LectureNaiveBayes)
3. [Stanford CS124 Lectures](http://www.stanford.edu/class/cs124/lec/naivebayes.pdf)