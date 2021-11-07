from django.forms import ModelForm
from copy import deepcopy

from dashboard.models.lab_entry_model import LabEntry
from dashboard.models.vehicle_model import VehicleModel, VEHICLE_META_FIELDS
from dashboard.models.customer_model import CustomerModel, CUSTOMER_MODEL_FIELDS


class VehicleMetaForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = list(VEHICLE_META_FIELDS)


class CustomerMetaForm(ModelForm):
    class Meta:
        model = CustomerModel
        fields = list(CUSTOMER_MODEL_FIELDS)


class ChildForms:
    NAME = 0
    FORM = 1
    POST = "POST"

    def __init__(self):
        self.__forms = {}

    def insert_form(self, name, creation_class):
        self.__forms[name] = creation_class

    def get_request_context(self):
        return {f[ChildForms.NAME]: f[ChildForms.FORM]() for f in self.__forms.items()}

    def get_forms_to_save(self, post_request):
        assert post_request.method == ChildForms.POST
        return {f[ChildForms.NAME]: f[ChildForms.FORM](post_request.POST) for f in self.__forms.items()}

    def get_forms(self):
        return deepcopy(self.__forms)


class LabEntryForm:

    def __init__(self):
        self.__child_forms = ChildForms()
        self.__child_forms.insert_form('vehicle', VehicleMetaForm)
        self.__child_forms.insert_form('customer', CustomerMetaForm)

    def save(self, request):
        forms_to_save = self.__child_forms.get_forms_to_save(request)
        if self.__are_valid(forms_to_save):
            self.__save(forms_to_save)
        else:
            pass

    def handle_get(self):
        return self.__child_forms.get_request_context()

    def forms_factory(self):
        return self.__child_forms.get_forms()

    @staticmethod
    def __are_valid(forms_to_save):
        ok = True
        for f in forms_to_save.values():
            ok &= f.is_valid()
        return ok

    @staticmethod
    def __save(forms_to_save):
        saved_instances = {form[ChildForms.NAME]: form[ChildForms.FORM].save() for form in forms_to_save.items()}
        new_lab_entry = LabEntry.create(**saved_instances)
        new_lab_entry.save()
