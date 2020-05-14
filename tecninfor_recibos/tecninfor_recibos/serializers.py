from rest_framework import serializers


from tecninfor_recibos.models import Empleados,Fechas,Login

# @app.route(f'{__url_base__}/empleado',methods=['GET'])
# def empleados():
#     session = Session()
#     try:
#         empleados_cursor = session.query(Empleados)
#         empleados_cursor = parse_request(Empleados,empleados_cursor,request)
#         resp = parse_to_json(empleados_cursor,Empleados)
#         return jsonify(resp)
#     except:
#         session.rollback()
#     finally:
#         session.close()

# @app.route(f'{__url_base__}/empleado/<cuil>')
# def get_empleados(cuil):
#     session = Session()
#     try:
#         empleados_cursor = session.query(Empleados).filter_by(**{'cuil':cuil})
#         resp = parse_to_json(empleados_cursor,Empleados,one=True)
#         return jsonify(resp)
#     except:
#         session.rollback()
#     finally:
#         session.close()

class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleados
        fields = '__all__'

