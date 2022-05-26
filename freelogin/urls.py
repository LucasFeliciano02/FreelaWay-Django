from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Apenas paths dos apps e nao das que são utilizadas como funções em views, pois essas pertencem ao proprio app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('autenticacao.urls')),
    path('jobs/', include('jobs.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #  ==  http://127.0.0.1:8000/media/referencias/imagem_3.png

# Url para arquivos estáticos, conforme ja estava setado no settings.py o (MEDIA_ROOT E O MEDIA_URL)  

#  meudominio.com.br/auth/
