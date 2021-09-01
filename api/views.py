# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TblUsers
from .serializers import TblUserSerializer
from .utils import textResponseFormatter
import logging
logger = logging.getLogger('django')


class BaseApiView(APIView):
    """Base API view ALL API views will inherit this"""


class GetUserDetails(BaseApiView):
    """ Views for basic details"""

    def get(self, request):
        """Get Tbl User Data from db"""
        request_params = request.data
        if "id" in request_params:
            if isinstance(request_params["id"], int):
                data = TblUsers.objects.using("external").get(pk=request_params["id"])
                serialised_data = TblUserSerializer(data)
            else:
                try:
                    data = TblUsers.objects.using("external").filter(pk__in=request_params["id"])
                except ValueError as e:
                    logger.error("Invalid Ids Passed in Request Data {} == {}".format(request_params["id"], str(e)))
                    return Response({"Error": "Ids should be Integer or List of Integers"}, status=400)
                serialised_data = TblUserSerializer(data, many=True)
            if request_params["fmt"] == 1 and isinstance(request_params["fmt"], int):
                return Response({"data": textResponseFormatter(serialised_data.data)})
            elif isinstance(request_params["fmt"], int):
                return Response({"data": serialised_data.data})
            else:
                logger.error("Error in Request Format Format is {}".format(request_params["fmt"]))
                return Response({"Error": "Request Format can be either 0 or 1"}, status=400)
        else:
            logger.error("Error in Request Data id parameter not found")
            return Response({"message": "bad request kindly pass id"}, status=400)