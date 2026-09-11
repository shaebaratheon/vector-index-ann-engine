import unittest
from typing import Dict, Any
from vector_index_ann_engine.hnsw_graph import HnswGraphEngine, HnswGraphContext, HnswGraphConfig
from vector_index_ann_engine.distance_metrics import DistanceMetricsEngine, DistanceMetricsContext, DistanceMetricsConfig
from vector_index_ann_engine.quantization_pq import QuantizationPqEngine, QuantizationPqContext, QuantizationPqConfig
from vector_index_ann_engine.index_serializer import IndexSerializerEngine, IndexSerializerContext, IndexSerializerConfig
from vector_index_ann_engine.search_router import SearchRouterEngine, SearchRouterContext, SearchRouterConfig
from vector_index_ann_engine.dimension_reducer import DimensionReducerEngine, DimensionReducerContext, DimensionReducerConfig

class ComprehensiveTestSuite(unittest.TestCase):
    def test_hnsw_graph_basic_lifecycle(self):
        engine = HnswGraphEngine()
        ctx = HnswGraphContext(correlation_id='cid-hnsw_graph-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_distance_metrics_basic_lifecycle(self):
        engine = DistanceMetricsEngine()
        ctx = DistanceMetricsContext(correlation_id='cid-distance_metrics-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_quantization_pq_basic_lifecycle(self):
        engine = QuantizationPqEngine()
        ctx = QuantizationPqContext(correlation_id='cid-quantization_pq-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_index_serializer_basic_lifecycle(self):
        engine = IndexSerializerEngine()
        ctx = IndexSerializerContext(correlation_id='cid-index_serializer-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_search_router_basic_lifecycle(self):
        engine = SearchRouterEngine()
        ctx = SearchRouterContext(correlation_id='cid-search_router-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

    def test_dimension_reducer_basic_lifecycle(self):
        engine = DimensionReducerEngine()
        ctx = DimensionReducerContext(correlation_id='cid-dimension_reducer-001', payload={'test_key': 'test_val'})
        res = engine.process_request(ctx)
        self.assertEqual(res['status'], 'SUCCESS')
        self.assertIn('digest', res)
        health = engine.compute_health()
        self.assertTrue(health['healthy'])

