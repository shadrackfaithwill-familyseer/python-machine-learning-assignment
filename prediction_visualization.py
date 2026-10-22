import matplotlib.pyplot as plt
import os
hours= ([1], [2], [3], [4], [5], [6], [7], [8], [9], [10])
exam_scores = (30, 40, 45, 55, 65, 70, 80, 85, 90, 95)
plt.scatter(hours, exam_scores, label="predicted score")
plt.title("Students Exam Score Prediction")
plt.ylabel("Hours")
plt.xlabel("predicted exam scores")
plt.grid(True)
plt.legend()
plt.savefig("Predicted_exam_scores.png", dpi=300, bbox_inches="tight")
print("image saved at:", os.path.abspath("predicted_exam_scores.png"))
plt.show()