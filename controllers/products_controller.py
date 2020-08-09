from flask import Blueprint, Flask, redirect, render_template, request
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.brand_repository as brand_repository
import repositories.product_type_repository as product_type_repository
