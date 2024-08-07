from django.shortcuts import render
from app.models import Category

# Create your views here.

def build_category_tree(categories):
    tree = []
    
    for category in categories:
        children = build_category_tree(category.children.all())
        tree.append({
            'id': category.id,
            'name': category.name,
            'children': children
        })
    return tree

def index(request):
    top_level_category = Category.objects.filter(parent=None)
    category_tree = build_category_tree(top_level_category)
    categories = Category.objects.all()
    return render(request, 'category.html', {'category_tree': category_tree})
