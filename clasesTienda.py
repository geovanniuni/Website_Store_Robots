class carritoCompra:
    fechaCreacion=None
    listaLineaProducto=None
  
    def __init__(self,fcx,lx=[]):
        self.__fechaCreacion=fcx
        self.listaLineaProducto=lx   
    def getFecha(self):
        return self.fechaCreacion
    def getListaLineas(self):
        return self.listaLineaProducto
    def addLineaProducto(self,newLine):
        self.listaLineaProducto.append(newLine)
    def getTotalCarrito(self):
        total=0
        for i in range(len(self.listaLineaProducto)):
            total+=self.listaLineaProducto[i].getPrecioLinea()
        return total
    def printCarrito(self):
        for i in range(len(self.listaLineaProducto)):
            self.listaLineaProducto[i].printLinea()
      
    

class lineaProducto:
    cantidad=None
    precioLinea=None
    productox=None
    def __init__(self,cantx,prox):
        self.cantidad=cantx
        self.productox=prox
        self.precioLinea=prox.getPrecioProducto()*cantx
        
    def getCantidad(self):
        return self.cantidad
    def getPrecioLinea(self):
        return self.precioLinea
    def getProductox(self):
        return self.productox
    
    def printLinea(self):
        print(self.productox.getDenominacion()+" "+str(self.cantidad), end=' ')
        print("$"+ str(self.productox.getPrecioProducto()), end=' ')
        print("$"+str(self.precioLinea))

class producto:
    idProducto=None
    denominacion=None
    proveedor=None
    precioProducto=None
    def __init__(self,idx,denox,provx,preciox):
        self.idProducto=idx
        self.denominacion=denox
        self.proveedor=provx
        self.precioProducto=preciox
    def getIdProducto(self):
        return self.idProducto
    def getDenominacion(self):
        return self.denominacion
    def getProveedor(self):
        return self.proveedor
    def getPrecioProducto(self):
        return self.precioProducto
        
class pedido:
    idPedido=None
    fechaRealizacion=None
    estado=None
    total=None
    carritox=None
    def __init__(self,idx,frx,fcx,lx):
        self.idPedido=idx
        self.fechaRealizacion=frx
        self.estado="Proceso"
        self.carritox=carritoCompra(fcx,lx)
    def getIdPedido(self):
        return self.idPedido
    def getFechaRealizacion(self):
        return self.fechaRealizacion
    def getEstado(self):
        return self.estado
    def getCarritox(self):
        return self.carritox
    def finalizarPedido(self):
        self.estado="Finalizado"
    def printPedido(self):
        print(self.idPedido,end=" ")
        print(self.estado,end=" ")
        print(self.fechaRealizacion)
        self.carritox.printCarrito()
        print("Total Pedido $"+str(self.carritox.getTotalCarrito()))
        print("\n")
    
        
class cliente:
    idCliente=None
    direccion=None
    telefono=None
    email=None
    listaPedidos=None
    def __init__(self,idx,dirx,telx,emailx):
        self.__idCliente=idx
        self.__direccion=dirx
        self.__telefono=telx
        self.__emailx=emailx
        self.listaPedidos=[]
        
    def getIdCliente(self):
        return self.idCliente
    def getDireccion(self):
        return self.direccion
    def getTelefono(self):
        return self.telefono
    def getEmail(self):
        return self.email
    def getPedidos(self):
        return self.listaPedidos
    def setPedidox(self,pedido):
        self.listaPedidos.append(pedido)
    def finalizarPedidox(self,idPedidox):
        for i in range(len(self.listaPedidos)):
            if(idPedidox==self.listaPedidos[i].getIdPedido()):
                self.listaPedidos[i].finalizarPedido()
    def testPedidos(self):
        for i in range(len(self.listaPedidos)):
            self.listaPedidos[i].printPedido()
            
    