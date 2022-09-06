
class Quiz(models.Model):
    title = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)




def __str__(self):
    return self.name

