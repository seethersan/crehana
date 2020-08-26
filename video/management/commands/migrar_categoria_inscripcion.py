from django.core.management.base import BaseCommand, CommandError
from django.db import connection

class Command(BaseCommand):
    help = 'Migra la informacion de la categoria e inscripcion al Progreso del video'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE video_progresovideo as vid
                SET categoria_id = (SELECT categoria_id FROM curso_curso as cur WHERE cur.id = vid.curso_id),
                inscripcion_id = (SELECT inscripcion_id FROM usuario_inscripcion as ins WHERE ins.usuario_id = vid.usuario_id AND ins.curso_id = vid.curso_id)
                """)