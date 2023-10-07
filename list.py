names = []
feedbacks = []
sumFeedback = 0
for i in range(5):
    name = input("Enter the name")
    feedback = int(input("Enter the Feedback"))
    names.append(name)
    feedbacks.append(feedback)
    sumFeedback = sumFeedback+feedback

average = sumFeedback/len(names)
print(average)
print(names)
print(feedbacks)