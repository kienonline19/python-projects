import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, mesage="Item not found.")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, mesage="Item not found.")

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        # item_data = request.get_json()

        if "price" not in item_data or "name" not in item_data:
            abort(
                400, message="Bad request. Ensure 'price' and 'name' are included in the JSON payload.")

        try:
            item = items[item_id]
            item |= item_data
            return item
        except KeyError:
            abort(404, message="Item not found.")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        # return {"items": list(items.values())}, 201
        return items.values()

    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):
        # item_data = request.get_json()
        """
        Here not only we need to validate data exists.
        But also what type of data. Price should be a float,
        for example.
        """

        """ if (
            "price" not in item_data or
            "store_id" not in item_data or
            "name" not in item_data
        ):
            abort(
                400,
                message="Bad request. Ensure 'price', 'store_id' and 'name' are included in the JSON payload."
            ) """

        for item in items.values():
            if (
                item_data["name"] == item["name"]
                and
                item_data["store_id"] == item["store_id"]
            ):
                abort(500, message="Item already exists.")

        if item_data["store_id"] not in stores:
            abort(404, mesage="Store not found.")

        item_id = uuid.uuid4().hex
        item = {**item_data, "id": item_id}
        items[item_id] = item
        return item, 201
