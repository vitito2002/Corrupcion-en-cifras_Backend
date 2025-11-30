import { useState, useEffect, useCallback } from 'react';

/**
 * Hook genérico para manejar datos de analytics
 * 
 * @template T - Tipo de datos que retorna la función fetch
 * @param fetchFn - Función que retorna una Promise con los datos
 * @param dependencies - Array de dependencias para el useEffect (opcional)
 * @param options - Opciones adicionales (autoFetch, initialData)
 * 
 * @returns Objeto con data, loading, error y función refetch
 * 
 * @example
 * ```tsx
 * const { data, loading, error, refetch } = useAnalytics(
 *   () => fetchCasosPorEstado(),
 *   []
 * );
 * ```
 */
export function useAnalytics<T>(
  fetchFn: () => Promise<T | null>,
  dependencies: any[] = [],
  options: {
    autoFetch?: boolean;
    initialData?: T | null;
  } = {}
) {
  const { autoFetch = true, initialData = null } = options;

  const [data, setData] = useState<T | null>(initialData);
  const [loading, setLoading] = useState<boolean>(autoFetch);
  const [error, setError] = useState<string | null>(null);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);

    try {
      const result = await fetchFn();
      setData(result);
      
      if (result === null) {
        setError('No se pudieron cargar los datos');
      }
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : 'Error desconocido al cargar los datos';
      setError(errorMessage);
      setData(null);
    } finally {
      setLoading(false);
    }
  }, [fetchFn]);

  useEffect(() => {
    if (autoFetch) {
      fetchData();
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, dependencies);

  const refetch = useCallback(() => {
    fetchData();
  }, [fetchData]);

  return {
    data,
    loading,
    error,
    refetch,
  };
}

