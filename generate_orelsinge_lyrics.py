import markovify


with open("corpus.txt") as corpus:
    text = corpus.read()

# Build the model.
model = markovify.NewlineText(text)

# Print five randomly-generated sentences
for i in range(20):
    print(model.make_sentence())

# Print three randomly-generated sentences of no more than 70 characters
for i in range(5):
    print(model.make_short_sentence(70))
