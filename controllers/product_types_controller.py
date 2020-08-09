from flask import Blueprint, Flask, redirect, render_template, request
from models.product_type import ProductType
import repositories.product_type_repository as product_type_repository