# from django.shortcuts import render
# from django.urls import reverse_lazy
# from django.db.models import Q 
# from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
# # from basic_app.forms import PostForm
# from basic_app.models import Post


# class IndexView(TemplateView):
#     template_name = 'basic_app/index.html'

# class ProductListView(ListView):
#     context_object_name = "products"
#     model = Post
#     template_name = "basic_app/product_list.html"
    
#     # applying filters
#     # def get_queryset(self): # new
#     #     return Post.objects.filter(
#     #         Q(com_name__icontains='Aerial') | Q(price__icontains=50)
#     #     )

#     def get_queryset(self): 
#         query = self.request.GET.get('q')

#         if query == None:
#             return Post.objects.all()
#         else:
#             object_list = Post.objects.filter(
#                 Q(com_name__icontains=query) | Q(price__icontains=query)
#             )
#             return object_list  


# class ProductDetailView(DetailView):
#     context_object_name = "product_detail"
#     model = Post
#     template_name = 'basic_app/product_detail.html'
    

# class ProductCreateView(CreateView):
#     fields = ("com_name", "price", "quantity", "create_date")
#     model = Post  


# class ProductUpdateView(UpdateView):
#     context_object_name = "product_detail"
#     fields = ("com_name", "price", "quantity", "create_date")
#     model = Post
    
    
# class ProductDeleteView(DeleteView):
#     context_object_name = "product"
#     model = Post
#     success_url = reverse_lazy("basic_app:list")
    


########################################################################################################
########################################################################################################



from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q 
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from basic_app.forms import PostForm, PeopleForm
from basic_app.models import Post, People
from datetime import datetime
import csv

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class ProductListView(ListView):
    context_object_name = "products"

    model = Post
    template_name = "basic_app/product_list.html"
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        query2 = self.request.GET.get('selected_date')
        query3 = self.request.GET.get('myDate')
        if query2:
            print(query2)
            # month_number = query2[:3]
            # year = query2[10:]
            # day = query2[6:8]
            # datetime_object = datetime.strptime(month_number, "%b")
            # month = datetime_object.month
            # time = f"{year}, {month}, {day}"
            # date_dt3 = datetime.strptime(time, '%Y, %m, %d')
            # date_dt3 = str(date_dt3)
            # date_dt3 = date_dt3[:10]
            object_list2 = Post.objects.filter(
                    Q(create_date__icontains=query2)
            )
            
            with open(f'{query2}.csv', 'w', newline='') as file:
                fieldnames = ['Item Name', 'Total price', 'quantity', 'Unit', 'create_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                day_purchase = 0

                for i in object_list2:
                    day_purchase += i.total_price 
                    writer.writerow({'Item Name': i.com_name, 'Total price': i.total_price, 'quantity': i.quantity,
                                     'Unit': i.unit, 'create_date': i.create_date})
                writer.writerow({'Item Name': 0, 'Total price': "Total Day purchase: "+str(day_purchase), 'quantity': 0,
                                'Unit': 0, 'create_date': 0})

        if query3:
            month = query3[:3]
            year = query3[-4:]
            datetime_object = datetime.strptime(month, "%b")
            month_number = datetime_object.month
            if month_number < 10:
                month_number = f"0{month_number}"
            time = f"{year}-{month_number}"
            print(time)

            object_list = Post.objects.filter(
                    Q(create_date__icontains=time)
            )
            print(object_list)

            with open(f'{query3}.csv', 'w', newline='') as file:
                fieldnames = ['Item Name', 'Total price', 'quantity', 'Unit' , 'create_date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                month_purchase = 0 

                for i in object_list:
                    month_purchase += i.total_price 
                    writer.writerow({'Item Name': i.com_name, 'Total price': i.total_price, 'quantity': i.quantity,
                                     'Unit': i.unit, 'create_date': i.create_date})
                writer.writerow({'Item Name': 0, 'Total price': 'Total Month Purchase: '+ str(month_purchase), 'quantity': 0,
                                     'Unit': 0, 'create_date': 0})



        if query == None:
            return Post.objects.all()
        else:
            object_list = Post.objects.filter(
                Q(com_name__icontains=query) | Q(total_price__icontains=query)
            )
            return object_list  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        objects = Post.objects.order_by().values_list('create_date', flat = True).distinct()
        dates = [i.date() for i in objects]
        unique_dates = set(dates)
        
        context['unique_dates'] = unique_dates
        return context
    

class ProductDetailView(DetailView):
    context_object_name = "product_detail"
    model = Post
    template_name = 'basic_app/product_detail.html'
    
    queryset = Post.objects.all()

    # def get_object(self):
    #     obj = super().get_object()
    #     # Record the last accessed date
    #     obj.total_price = obj.price * obj.quantity
    #     obj.save()
    #     return obj

class ProductCreateView(CreateView):
    # fields = ("com_name", "price", "quantity", "unit", "create_date")
    form_class = PostForm
    model = Post  


class ProductUpdateView(UpdateView):
    context_object_name = "product_detail"
    # fields = ("com_name", "price", "quantity", "create_date")
    
    form_class = PostForm
    model = Post
    
    
class ProductDeleteView(DeleteView):
    context_object_name = "product"
    
    model = Post
    success_url = reverse_lazy("basic_app:list")
    

#####################################################
####### Building Employee side view #################


class PeopleListView(ListView):
    context_object_name = "peoples"

    model = People
    template_name = "basic_app/people_list.html"

    def get_queryset(self): 
        query = self.request.GET.get('query')

        query2 = self.request.GET.get('selected_date')
        query3 = self.request.GET.get('myDate')
        if query2:
            
            object_list2 = People.objects.filter(
                    Q(date__icontains=query2)
            )
            
            with open(f'Hisaab-{query2}.csv', 'w', newline='') as file:
                fieldnames = ['Person Name', 'Total Bill', 'Paid Money', 'Rem Money', 'Item Name', 'Date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                total_day_bill = 0
                total_paid_amount = 0
                total_day_debt = 0

                for i in object_list2:
                    total_day_bill += i.total_bill
                    total_paid_amount += i.paid_money
                    total_day_debt += i.rem_money
                     
                    writer.writerow({'Person Name': i.name, 'Total Bill': i.total_bill, 'Paid Money': i.paid_money,
                                     'Rem Money': i.rem_money, 'Item Name': i.item_name, 'Date': i.date})
                writer.writerow({'Person Name': 0, 'Total Bill': "Total Day Bill : "+ str(total_day_bill), 'Paid Money': "Total Paid Amount : "+ str(total_paid_amount),
                                     'Rem Money': "Total Day Debt : "+ str(total_day_debt), 'Item Name': 0, 'Date': 0})
                

        if query3:
            month = query3[:3]
            year = query3[-4:]
            datetime_object = datetime.strptime(month, "%b")
            month_number = datetime_object.month
            if month_number < 10:
                month_number = f"0{month_number}"
            time = f"{year}-{month_number}"
            print(time)

            object_list2 = People.objects.filter(
                    Q(date__icontains=time)
            )
            
            with open(f'Hisaab-{query3}.csv', 'w', newline='') as file:
                fieldnames = ['Person Name', 'Total Bill', 'Paid Money', 'Rem Money', 'Item Name', 'Date']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                total_month_bill = 0
                total_paid_amount = 0
                total_month_debt = 0

                for i in object_list2:
                    total_month_bill += i.total_bill
                    total_paid_amount += i.paid_money
                    total_month_debt += i.rem_money
                     
                    writer.writerow({'Person Name': i.name, 'Total Bill': i.total_bill, 'Paid Money': i.paid_money,
                                     'Rem Money': i.rem_money, 'Item Name': i.item_name, 'Date': i.date})
                writer.writerow({'Person Name': 0, 'Total Bill': "Total Month Bill : "+ str(total_month_bill), 'Paid Money': "Total Month Paid Amount : "+ str(total_paid_amount),
                                     'Rem Money': "Total Month Debt : "+ str(total_month_debt), 'Item Name': 0, 'Date': 0})




        if query == None:
            return People.objects.all()
        else:
            object_list = People.objects.filter(
                Q(name__icontains=query) | Q(total_bill__icontains=query)
            )
            return object_list  



class PeopleDetailView(DetailView):
    context_object_name = "people_detail"
    model = People
    template_name = 'basic_app/people_detail.html'

    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.rem_money = obj.total_bill - obj.paid_money
        obj.save()
        return obj


class PeopleCreateView(CreateView):
    form_class = PeopleForm
    model = People  


class PeopleUpdateView(UpdateView):
    context_object_name = "people_detail"
    
    form_class = PeopleForm
    model = People
    
    
class PeopleDeleteView(DeleteView):
    context_object_name = "people"
    
    model = People
    success_url = reverse_lazy("basic_app:people_list")
    















