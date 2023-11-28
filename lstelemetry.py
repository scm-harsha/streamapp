import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

# export these two as environment variables
# export GRPC_TRACE=http,call_error,connectivity_state
# export LS_ACCESS_TOKEN="your-access-token"


def __init__(self):
    LoggingInstrumentor().instrument()


def get_otlp_exporter():
    ls_access_token = os.environ.get("LS_ACCESS_TOKEN")
    return OTLPSpanExporter(
        endpoint="ingest.lightstep.com:443",
        headers=(("lightstep-access-token", ls_access_token),),
    )


def create_tracer(service_name):
    span_exporter = get_otlp_exporter()

    provider = TracerProvider()
    if not os.environ.get("OTEL_RESOURCE_ATTRIBUTES"):
        # Service name is required for most backends
        resource = Resource(attributes={SERVICE_NAME: service_name})
        provider = TracerProvider(resource=resource)
        print("Using default service name")

    processor = BatchSpanProcessor(span_exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)

    return trace.get_tracer(__name__)
