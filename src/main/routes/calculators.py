from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory
from src.main.factories.calculator3_factory import calculator3_factory

from src.errors.error_controller import handle_errors

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)

        return jsonify(response) 
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response["status_code"]

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response["status_code"]

@calc_route_bp.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)

        return jsonify(response)
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response['body']), error_response["status_code"]
    
@calc_route_bp.route("/calculator/4", methods=["POST"])
def calculator_4():
    try:
        dados = request.json
        numbers = dados.get('numbers')

        # Verifica se a lista está presente e se contém apenas números válidos
        if not numbers or not all(isinstance(num, (int, float)) for num in numbers):
            return jsonify({'message': 'Invalid numbers'}), 400
        
        media = sum(numbers ) / len(numbers) # media

        return jsonify({'media': media})
    
    except Exception as e:
        return jsonify({"erro": str(e)}), 500  