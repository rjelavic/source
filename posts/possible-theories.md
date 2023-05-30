# The space of possible metaphysical theories of everything

## Time

You, right now, are experiencing something.
This sensory experience could in fact be the only thing which ever existed and will ever exist.
There was no past, there is no future, there are no other experiences other than this right now.
This position of radical solipsism can't be conclusively ruled out.
Assuming that position is true, not much can be built from it - it is what it is.
One more implication of that position is that all memories which you may be recalling right now are not of the past, since there is no past.
Our first axiom:

1. Time exists

The only other theory of everything which does not have this as an axiom is what we called radical solipsism.

## Experience

The starting point of our analysis is our conscious experience.
This is the only thing we have direct knowledge of.
We do not see the objects around us directly.
What we percieve are colors and shapes, from which we infer the existence of external objects.
Any other way to start our analysis would be to start from something we don't have direct, but only indirect, knowledge of.

## Strings

What is the optimal way to construct a model of the world from our experience?
To answer that question, we need to talk about experience.
In order to talk about experience, we need to transform experience into some array of symbols.
Commonly, this is done with words, or to use a technical term, with natural language.
An array of symbols is called a string.
Generally, the experience can be encoded into some array in an infinite number of ways.
On computers, for example, you can encode images as png, jpg, etc.

## Models

This encoding could be performed for all experiences you ever had from the time you are born until now.
You don't remember every single thing, but in principle, it could be done.
Once we have our string, a natural question occurs, which process generated the string?

One possibility is that the string is just random, there are no patterns in it.
Technically, we would say the string is incompressible.
The process which generated it could very well as be just a random noise generator.

We could also say that it's simply impossible to comprehend what generated it.
The process is unlike anything we could imagine and it's all just a big mistery.

Or, we could notice patterns in the experience, and as such in the string, and we could try to understand it.
Thus, we need a language for describing processes.
One such language could be a one which describes something similar to deterministic finite automata.
The machine can be in only one state at a time.
There are also arrows connecting some states to other states, each arrow represents a state transition.
Along with each state transition, there is a string which is being printed.

todo example

These kinds of machines are very limited, for example there is no simple way to make them output the first _n_ natural numbers, except hardcoding them.
We could use pushdown automata but they suffer from the same kind of limitations.

todo example

The Turing machine, or a Turing-complete programming language, as the most powerful of all automata, due to Church-Turing thesis, seems like a natural choice.
It also has a property of invariance, which is too technical to get into details, the point of which being: it's irrelevant which programming language we choose.

todo example

The choice of some automata as a language for desribing processes, limits us to countable structures.
If reality is isomorphic to some automaton, then it is countable.
The string which describes our experience is countable, our thoughts are countable, axioms are countable, theorems are countable, and algorithms are countable.
Thus, even if reality were an uncountable structure, the best we could do is to approximate it with some countable model.

## Probability

Once we have a language for desribing processes, we face the next challange: there is an infinity of models which are consistent with generating our string as output.
Thus, we need a probability distribution on all such consistent models.
If we have a prior distribution, Bayes theorem gives us a law of how to update that distribution based on new experience i.e. our string getting longer.
This prior distribution can be based on some property of our models.
Some natural properties in case of programs are length, memory and speed.

## Existence

Now we have our infinity of models and a probability distribution on them.
The question is, do all of those models have the same ontological status.
We could say they all exist, and the probability just tells us what is the probability of us appearing in them.
Or we could say that just one model exists and the probability gives us the credence we assign to some particular model being the true one.

