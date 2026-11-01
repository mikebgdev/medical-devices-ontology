# Medical Devices Ontology

Ontología de dispositivos médicos en RDF, con documentación HTML generada y visualización WebVOWL. Las serializaciones y documentación están en `docs/`. Abrir `docs/index-en.html` para consultar las clases y propiedades. El repositorio no contiene una aplicación clínica ni ofrece recomendaciones médicas.

<!-- repository-quality-20261101 -->
 ## Comprobaciones y publicación

 La verificación del repositorio está en `ci/verify.sh`. Necesita las dependencias de desarrollo descritas arriba; no utiliza datos ni credenciales de producción.

 ```sh
 bash ci/verify.sh
 ```

 El workflow **Quality** comprueba secretos y después ejecuta esas comprobaciones en pushes a la rama principal y en pull requests. El escaneo usa Gitleaks 8.30.1 con descarga verificada por SHA256; examina el historial Git disponible y el directorio actual. No imprime valores de secretos. Para la revisión completa local, usar un clon con historial completo y ejecutar `bash ci/check_secrets.sh`; se puede indicar `GITLEAKS_BIN` con esa versión instalada.

 La existencia del archivo de workflow no acredita que el runner esté disponible ni que la revisión haya pasado. Antes de integrar, comprobar los resultados **Secrets** y **Verify** del mismo SHA. Este workflow no despliega servicios. Conservar el procedimiento de entrega y rollback específico del proyecto.


<!-- license-adopted-20261101 -->
## Licencia

**CC-BY-4.0**, con el alcance indicado en [docs/LICENSING.md](docs/LICENSING.md). El texto completo está en [LICENSE](LICENSE). La concesión cubre las aportaciones propias; los recursos y componentes de terceros conservan sus licencias y atribuciones.
