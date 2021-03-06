import _plotly_utils.basevalidators


class SizesrcValidator(_plotly_utils.basevalidators.SrcValidator):

    def __init__(
        self, plotly_name='sizesrc', parent_name='area.marker', **kwargs
    ):
        super(SizesrcValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='none',
            role='info',
            **kwargs
        )
