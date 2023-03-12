from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=255)
    User_email = models.CharField(max_length=255)
    User_created_at = models.DateTimeField(auto_now_add=True)
    User_updated_at = models.DateTimeField(auto_now=True)
    User_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.User_name
    



    
class ExpanseGroup(models.Model):
    id = models.AutoField(primary_key=True)
    ExpanseGroup_name = models.CharField(max_length=255)
    ExpanseGroup_description = models.TextField(null=True, blank=True)
    ExpanseGroup_created_at = models.DateTimeField(auto_now_add=True)
    ExpanseGroup_updated_at = models.DateTimeField(auto_now=True)
    ExpanseGroup_image = models.TextField(null=True, blank=True)
    ExpanseGroup_amount = models.TextField(null=True, blank=True, default="0")
    ExpanseGroup_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ExpanseGroup_name
    


class LinkExpanseGroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    LinkExpanseGroupUser_group_id = models.ForeignKey(ExpanseGroup, on_delete=models.CASCADE, related_name="LinkExpanseGroupUser_group_id")
    LinkExpanseGroupUser_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="LinkExpanseGroupUser_user_id")
    LinkExpanseGroupUser_created_at = models.DateTimeField(auto_now_add=True)
    LinkExpanseGroupUser_updated_at = models.DateTimeField(auto_now=True)
    LinkExpanseGroupUser_is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.LinkExpanseGroupUser_group_id.ExpanseGroup_name + " " + self.LinkExpanseGroupUser_user_id.User_name

class ExpanseGroupUser(models.Model):
    id = models.AutoField(primary_key=True)
    ExpanseGroupUser_group_id = models.ForeignKey(ExpanseGroup, on_delete=models.CASCADE, related_name="ExpanseGroupUser_group_id")
    ExpanseGroupUser_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    ExpanseGroupUser_created_at = models.DateTimeField(auto_now_add=True)
    ExpanseGroupUser_updated_at = models.DateTimeField(auto_now=True)
    ExpanseGroupUser_is_active = models.BooleanField(default=True)
    ExpanseGroupUser_amount = models.TextField(null=True, blank=True, default="0")
    ExpanseGroupUser_description = models.TextField(null=True, blank=True)
    ExpanseGroupUser_Note = models.TextField(null=True, blank=True)
    ExpanseGroupUser_Name=models.CharField(max_length=255,null=True, blank=True)




    def __str__(self):
        return "name"




class Expanse(models.Model):
    id = models.AutoField(primary_key=True,)
    Expanse_name=models.CharField(max_length=255,null=True, blank=True)
    Expanse_created_at = models.DateTimeField(auto_now_add=True)
    Expanse_updated_at = models.DateTimeField(auto_now=True)
    Expanseamount = models.TextField(null=True, blank=True, default="0")
    Expanse_is_active = models.BooleanField(default=True)
    Expanse_description = models.TextField(null=True, blank=True)
    Expanse_Note = models.TextField(null=True, blank=True)
    Expanse_Location = models.CharField(max_length=255, null=True, blank=True)
    Expanse_locationName = models.CharField(max_length=255, null=True, blank=True)
    Expanse_locationAddress = models.CharField(max_length=255, null=True, blank=True)
    Expanse_locationCity = models.CharField(max_length=255, null=True, blank=True)
    Expanse_locationState = models.CharField(max_length=255, null=True, blank=True)
    Expanse_locationCountry = models.CharField(max_length=255, null=True, blank=True)
    Expanse_group_id = models.ForeignKey(ExpanseGroupUser, on_delete=models.CASCADE, related_name="Expanse_group_id")
    Expanse_user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Expanse_user_id")

    def __str__(self):
        return "ExpanseGroupUser"
    







# class ExpanseGroup(models.Model):
#     id = models.AutoField(primary_key=True)
#     ExpanseGroup_name = models.CharField(max_length=255)
#     ExpanseGroup_description = models.TextField(null=True, blank=True)
#     ExpanseGroup_created_at = models.DateTimeField(auto_now_add=True)
#     ExpanseGroup_updated_at = models.DateTimeField(auto_now=True)
#     ExpanseGroup_image = models.TextField(null=True, blank=True)
#     ExpanseGroup_amount = models.TextField(null=True, blank=True, default="0")
#     ExpanseGroup_is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.ExpanseGroup_name





# class Expanse(models.Model):
#     id = models.AutoField(primary_key=True)
#     Expanse_name = models.CharField(max_length=255)
#     Expanse_description = models.TextField(null=True, blank=True)
#     Expanse_created_at = models.DateTimeField(auto_now_add=True)
#     Expanse_updated_at = models.DateTimeField(auto_now=True)
#     Expanse_image = models.TextField(null=True, blank=True)
#     Expanse_amount = models.TextField(null=True, blank=True, default="0")
#     Expanse_Note = models.TextField(null=True, blank=True)
#     Expanse_Location = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_locationName = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_locationAddress = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_locationCity = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_locationState = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_locationCountry = models.CharField(max_length=255, null=True, blank=True)
#     Expanse_group_name = models.CharField(max_length=255, null=True, blank=True)
#     ExpanseGroup_id = models.ForeignKey(ExpanseGroup, on_delete=models.CASCADE, related_name="ExpanseGroup_id")
#     Expanse_is_active = models.BooleanField(default=True)


#     def __str__(self):
#         return self.Expanse_name
    


# class ExpanseGroupUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     ExpanseGroupUser_name = models.CharField(max_length=255)
#     ExpanseGroupUser_email = models.CharField(max_length=255)
#     ExpanseGroupUser_created_at = models.DateTimeField(auto_now_add=True)
#     ExpanseGroupUser_updated_at = models.DateTimeField(auto_now=True)
#     ExpanseGroupUser_image = models.TextField(null=True, blank=True)
#     ExpanseGroupUser_is_active = models.BooleanField(default=True)
#     ExpanseGroupUser_group_id = models.ForeignKey(ExpanseGroup, on_delete=models.CASCADE, related_name="ExpanseGroupUser_group_id")

#     def __str__(self):
#         return self.ExpanseGroupUser_name
    

# class ExpanseUser(models.Model):
#     id = models.AutoField(primary_key=True)
#     ExpanseUser_amount = models.TextField(null=True, blank=True, default="0")
#     ExpanseUser_created_at = models.DateTimeField(auto_now_add=True)
#     ExpanseUser_updated_at = models.DateTimeField(auto_now=True)
#     ExpanseUser_group_user_id = models.ForeignKey(ExpanseGroupUser, on_delete=models.SET_NULL, related_name="ExpanseUser_group_user_id",null=True, blank=True)
#     ExpanseUser_group_id = models.ForeignKey(ExpanseGroup, on_delete=models.CASCADE, related_name="ExpanseUser_group_id")
#     ExpanseUser_expanse_id = models.ForeignKey(Expanse, on_delete=models.CASCADE, related_name="ExpanseUser_expanse_id")

#     def __str__(self):
#         return self.ExpanseUser_amount
    

