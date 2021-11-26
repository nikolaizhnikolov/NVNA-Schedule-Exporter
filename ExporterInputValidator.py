from QueryTypes import QueryTypes

class ExporterInputValidator:
    def validate_group(group, queryType):
        if(type(group) != int or type(queryType) != str):
            return False
        elif queryType == QueryTypes.GROUP.value:
            #TODO
            return
        elif queryType == QueryTypes.LECTURER.value:
            #TODO
            return
        elif queryType == QueryTypes.WEEK.value:
            #TODO
            return;

    def validate_query_type(queryType):
        if(type(queryType) != str):
            return False
        elif queryType == QueryTypes.GROUP.value or \
            queryType == QueryTypes.LECTURER.value or \
            queryType == QueryTypes.WEEK.value:
            return True
        else: 
            return False

    def validate_week(week):        
        if(int(week) == 0):
            return False
        elif(int(week) > 0 and int(week) <53):
            return True
        else:
            return False
        