# Rock Paper Scissor Prediction using Bayesian probability

Course Description:
- Course: Machine Learning, Summer 2019
- Grade: A
- Program: Master of Science
- Major: Computer Science
- Department of Computer Science and Mathematics
- University of Central Missouri

Machine Learning course final project written to enter and play [RPS](http://www.rpscontest.com/) programming competition. Additionally, competed in a class tournament with 15 other teams, winning 250 games of 300 and securing the second place.

#### **Rock-Paper-Scissor**
Rock paper scissors is a hand game usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. These shapes are "rock", "paper", and "scissors".

#### **Bayes's Theorem**
Bayes's theorem describes the probability of an event, based on prior knowledge of conditions that might be related to the event.

#### **Bayes's Theorem formula**
![Bayes's Theorem](https://katkamrakesh.github.io/rock_paper_scissor_prediction/img/bayes_theorem.png)

###### Equivalently, Bayes Theorem can be written as:
posterior = likelihood * prior / evidence

**Working**
The program predicts the next move based on the previous moves, calculating the probability/likelihood of outcomes for rock, paper and scissor. Initially, the program will output ***R,P,S*** randomly for starting 3 rounds. Post starting 3 rounds, the Bayes' probability logics kicks in and calculate the likely outcome based on chain of previous 3 events, the opponent outcome of those events and number of occurance of similar events.
