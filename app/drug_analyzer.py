class DrugAnalyzer():
    data = []

    def __init__(self, data=None):
        if data is not None:
            self.data = data

    def __add__(self, value):
        if not isinstance(value, list):
            raise ValueError('Improper type of the added variable.')
        if len(value) != 4:
            raise ValueError('Improper length of the added list.')
        self.data.append(value)
        return self

    def verify_series(
            self,
            series_id: str,
            act_subst_wgt: float,
            act_subst_rate: float,
            allowed_imp: float) -> bool:

        def filter(self, series_id):
            result = []
            for drug in self.data:
                if drug[0].split('-')[0] == series_id:
                    result.append(drug)
            return result

        def verify_act_subst_wgt(drugs, act_subst_wgt, act_subst_rate):
            min_subst_wgt = len(drugs) * act_subst_wgt * (1 - act_subst_rate)
            max_subst_wgt = len(drugs) * act_subst_wgt * (1 + act_subst_rate)
            if (total_active_substance < min_subst_wgt or
                    total_active_substance > max_subst_wgt):
                return False
            return True

        def verify_impurities_wgt(
                total_impurities, total_pill_weight, allowed_imp):
            if total_impurities > total_pill_weight * allowed_imp:
                return False
            return True

        # Filter by series_id
        valid_drugs = filter(self, series_id)
        # Raise ValueError if series_id is not present in the data at all
        if not valid_drugs:
            text = '{} series is not present within the dataset.'
            msg = text.format(series_id)
            raise ValueError(msg)
        # Calculate total values
        total_pill_weight, total_active_substance, total_impurities = 0, 0, 0
        for drug in valid_drugs:
            total_pill_weight += drug[1]
            total_active_substance += drug[2]
            total_impurities += drug[3]
        # Verify active substance weight
        if not verify_act_subst_wgt(
                valid_drugs, act_subst_wgt, act_subst_rate):
            return False
        # Verify impurities weight
        if not verify_impurities_wgt(
                total_impurities, total_pill_weight, allowed_imp):
            return False
        return True
