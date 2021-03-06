import _plotly_utils.basevalidators


class ThicknessmodeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='thicknessmode',
        parent_name='parcoords.line.colorbar',
        **kwargs
    ):
        super(ThicknessmodeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='colorbars',
            role='style',
            values=['fraction', 'pixels'],
            **kwargs
        )
