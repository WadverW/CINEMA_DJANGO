# from django.db import models
# from django.contrib.auth import get_user_model
#
# User = get_user_model()
#
# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     screening = models.ForeignKey("cinema_app.Screening", on_delete=models.CASCADE)
#     seat = models.ForeignKey("cinema_app.Seat", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     is_paid = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f"{self.user.username} - {self.screening.showtime} - {self.seat}"
#
#     class Meta:
#         ordering = ['-created_at']
#         constraints = [
#             models.UniqueConstraint(fields=['screening', 'seat'], name='unique_booking')
#         ]
