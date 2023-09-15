from manim import *
#from library.utils import *

texTypes = str | Text | Tex | MathTex

class BasicGraphDict(VDict):
    def __init__(self, xrange:list[float] = [-1, 1, 1], yrange:list[float] = [-1, 1, 1],
                 xLengthRatio:float = 1, yLengthRatio:float = 1,
                 xLabelTex : None | texTypes = None,
                 yLabelTex : None | texTypes = None,
                 hideXAxis : bool = False, hideYAxis : bool = False,
                 func = None, graphXRange:list[float] = None,
                 graphLabelTex : None | texTypes = None,
                 axKey = "ax", xLabelKey = "xLabel", yLabelKey = "yLabel", graphKey = "graph", graphLabelKey = "graphLabel",
                 texScaleRatio = 1, **ax_kwargs):
        '''
        VDict contains basic ax, xLabel, yLabel, graph, graphLabel.
        '''
        self.axKey = axKey
        self.xLabelKey = xLabelKey
        self.yLabelKey = yLabelKey
        self.graphKey = graphKey
        self.graphLabelKey = graphLabelKey
        self.texScaleRatio = texScaleRatio
        
        super().__init__()
        self.buildAx(xrange, yrange, hideXAxis, hideYAxis, xLengthRatio, yLengthRatio, **ax_kwargs)
        self.buildAxLabel(xLabelTex, yLabelTex)
        if hideXAxis: self.remove(self.xLabelKey)
        if hideYAxis: self.remove(self.yLabelKey)
        if func is not None:
            self.buildGraph(func, graphLabelTex, graphXRange)
    
    def buildAx(self, xrange:list[float]=[-1,1,1], yrange:list[float]=[-1,1,1],
                hideXAxis : bool = False, hideYAxis : bool = False,
                xLengthRatio:float = 1, yLengthRatio:float = 1,
                axKey : None | str = None,
                **ax_kwargs):
        '''
        Create a 1:1 ratio coordinate plane that fits the given range of x and y.
        '''
        if axKey is None: axKey = self.axKey
        if hideXAxis: ax_kwargs["x_axis_config"] = {"include_tip": False, "stroke_width": 0}
        if hideYAxis: ax_kwargs["y_axis_config"] = {"include_tip": False, "stroke_width": 0}
        self[axKey] = Axes(x_range=xrange, y_range=yrange,
              x_length=(xrange[1] - xrange[0])*xLengthRatio, 
              y_length=(yrange[1] - yrange[0])*yLengthRatio,
              axis_config={
              "include_tip": True,
              "tip_width": 0.1,
              "tip_height": 0.15,
              "include_ticks": False,
              "include_numbers": False},
              **ax_kwargs)
        return self[axKey]
    
    def buildAxLabel(self, xLabelTex : None | texTypes = None, yLabelTex : None | texTypes = None, 
                     xLabelKey : None | str = None, yLabelKey : None | str = None, axKey : None | str = None):
        return self.buildXAxLabel(xLabelTex, xLabelKey, axKey), self.buildYAxLabel(yLabelTex, yLabelKey, axKey)

    def buildXAxLabel(self, xLabelTex : None | texTypes, xLabelKey : None | str = None, axKey : None | str = None):
        if xLabelKey is None: xLabelKey = self.xLabelKey
        if axKey is None: axKey = self.axKey
        if xLabelTex is None: xLabelTex = "$x$"
        if type(xLabelTex) is str:
            xLabelTex = Tex(xLabelTex)
        self[xLabelKey] = self[axKey].get_x_axis_label(xLabelTex, direction=RIGHT).scale(self.getScaleRatio()*self.texScaleRatio)
        return self[xLabelKey]

    def buildYAxLabel(self, yLabelTex : None | texTypes, yLabelKey : None | str = None, axKey : None | str = None):
        if yLabelKey is None: yLabelKey = self.yLabelKey
        if axKey is None: axKey = self.axKey
        if yLabelTex is None: yLabelTex = "$y$"
        if type(yLabelTex) is str:
            yLabelTex = Tex(yLabelTex)
        self[yLabelKey] = self[axKey].get_y_axis_label(yLabelTex, direction=UP).scale(self.getScaleRatio()*self.texScaleRatio)
        return self[yLabelKey]
    
    def buildGraph(self, func, labelTex : None | texTypes = None, 
                   xRange : None | list[float] = None,
                   graphKey : None | str = None, graphLabelKey : None | str = None, axKey : None | str = None, **kwargs):
        '''
        Create a graph of the given function.
        '''
        if graphKey is None: graphKey = self.graphKey
        if graphLabelKey is None: graphLabelKey = self.graphLabelKey
        if axKey is None: axKey = self.axKey
        self[graphKey] = self[axKey].plot(func, xRange, **kwargs)

        if labelTex is not None:
            return self[graphKey], self.buildGraphLabel(labelTex, graphKey, graphLabelKey)
        return self[graphKey]

    def buildGraphLabel(self, labelTex : texTypes, 
                        graphKey : None | str = None, graphLabelKey : None | str = None, axKey : None | str = None,
                        **kwargs):
        if graphKey is None : graphKey = self.graphKey
        if graphLabelKey is None : graphLabelKey = self.graphLabelKey
        if axKey is None : axKey = self.axKey
        if type(labelTex) is str: 
            labelTex = Tex(labelTex)
        self[graphLabelKey] = self[axKey].get_graph_label(self[graphKey], labelTex.scale(self.getScaleRatio()*self.texScaleRatio), **kwargs)
        return self[graphLabelKey]

    def buildDotOnAxLabel(self, val: float | ValueTracker, label: None | texTypes = None, 
                          isOnX: bool = True, buff : float = 0.2,
                          axKey : None | str = None, labelKey : None | str = None):
        if labelKey is None: labelKey = "labelOn"+str(val)

        if axKey is None : axKey = self.axKey
        if label is None: label = str(val)
        if type(label) is str: label = Tex(label)

        label.scale(self.getScaleRatio()*self.texScaleRatio)

        if type(val) is ValueTracker:
            if isOnX:
                self[labelKey] = label.add_updater(lambda m: m.next_to(self[axKey].coords_to_point(val.get_value(), -buff), DOWN, aligned_edge=UP, buff=0))
            else:
                self[labelKey] = label.add_updater(lambda m: m.next_to(self[axKey].coords_to_point(-buff, val.get_value()), DOWN, aligned_edge=UP, buff=0))
        else:
            if isOnX:
                self[labelKey] = label.next_to(self[axKey].coords_to_point(val, -buff), DOWN, aligned_edge=UP, buff=0)
            else:
                self[labelKey] = label.next_to(self[axKey].coords_to_point(-buff, val), DOWN, aligned_edge=UP, buff=0)
        return self[labelKey]
    
    def buildLine(self, lineKey: str, startCoordinate: slice, endCoordinate: slice, axKey : None | str = None, 
                  isDashedLine=False, isArrow=False, stroke_width=2, max_tip_length_to_length_ratio=0.03, **kwargs):
        if axKey is None : axKey = self.axKey
        startPoint = self[axKey].c2p(*startCoordinate)
        endPoint = self[axKey].c2p(*endCoordinate)
        if isDashedLine:
            self[lineKey] = DashedLine(startPoint, endPoint, stroke_width=stroke_width, **kwargs)
        elif isArrow:
            self[lineKey] = Arrow(startPoint, endPoint, stroke_width=stroke_width, max_tip_length_to_length_ratio=max_tip_length_to_length_ratio, **kwargs)
        else:
            self[lineKey] = Line(startPoint, endPoint, stroke_width=stroke_width, **kwargs)

    
    def getScaleRatio(self):
        return Line(self["ax"].c2p(0, 0), self["ax"].c2p(1, 0)).get_length()
