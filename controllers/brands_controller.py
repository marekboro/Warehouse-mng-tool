from flask import Blueprint, Flask, redirect, render_template, request
from models.brand import Brand
import repositories.brand_repository as brand_repository