
from rest_framework import serializers
from goods.models import Goods,GoodsCategory

class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerialize()
    class Meta:
        model = Goods
        fields = "__all__"
        # fields = ('name', 'click_num', 'market_price', 'add_time')
