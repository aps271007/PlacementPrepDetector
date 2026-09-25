import io
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import DocumentStream, InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions

#disable heavy ML OCR 
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False

 #converter initliazed globally to make sure it doesn't get reinitialized upon every new file upload causing massive memory spikes and latency
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)


def fileconverter(source: bytes, filename: str):
    """Need to read the input(bytes file) in BytesIO stream to wrap it as an in memory buffer
    Then convert the memory buffer into DocumentStream object which can then be converted to a docling document
   This docling document can be converted into any file format such as markdown, json,html etc. """

    #wrapping
    buffer = io.BytesIO(source)
    #conversion to documentstream object
    doc_stream = DocumentStream(name=filename, stream=buffer)
    #coversion to docling document
    md_file = converter.convert(doc_stream).document
    #to markdown
    return md_file.export_to_markdown()