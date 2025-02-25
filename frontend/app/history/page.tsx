'use client'

import React, { useEffect, useState } from 'react'
import axios from 'axios'

const HistoryPage = () => {
  const [records, setRecords] = useState([])
  const [page, setPage] = useState(1)
  const [search, setSearch] = useState('')
  const [totalPages, setTotalPages] = useState(1)

  useEffect(() => {
    const fetchRecords = async () => {
      try {
        const response = await axios.get('http://localhost:8000/history', {
          params: { page, search_by_path: search } // Changed to search by result image path
        })
        setRecords(response.data.records)
        setTotalPages(response.data.total_pages)
      } catch (error) {
        console.error('Error fetching history records', error)
      }
    }

    fetchRecords()
  }, [page, search])

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <h1 className="text-3xl font-extrabold mb-6 text-black text-center">History Records</h1>

      <input
        type="text"
        placeholder="Search by result image path..." // Updated search placeholder
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        className="block w-full p-2 mb-4 border rounded-lg text-black"
      />

      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow-lg rounded-lg">
          <thead>
            <tr className="bg-gray-200">
              <th className="p-4 text-black text-left">Time</th>
              <th className="p-4 text-black text-left">People Count</th>
              <th className="p-4 text-black text-left">Image</th>
              <th className="p-4 text-black text-left">Result Image Path</th>
            </tr>
          </thead>
          <tbody>
            {records.map((record) => (
              <tr key={record.id} className="border-t">
                <td className="p-4 text-black align-middle">{new Date(record.time).toLocaleString()}</td>
                <td className="p-4 text-black align-middle">{record.num_bboxes}</td>
                <td className="p-4 align-middle">
                  <img
                    src={`http://localhost:8000/${record.result_image_file_path}`}
                    alt="Processed result"
                    className="w-32 h-32 object-cover rounded-lg"
                  />
                </td>
                <td className="p-4 text-black align-middle">{record.result_image_file_path}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex justify-center mt-4">
        <button
          disabled={page <= 1}
          onClick={() => setPage(page - 1)}
          className="p-2 mx-2 bg-blue-500 text-white rounded-lg disabled:bg-gray-400"
        >
          Previous
        </button>
        <span className="p-2 text-black">Page {page}</span>
        <button
          disabled={page >= totalPages}
          onClick={() => setPage(page + 1)}
          className="p-2 mx-2 bg-blue-500 text-white rounded-lg disabled:bg-gray-400"
        >
          Next
        </button>
      </div>
    </div>
  )
}

export default HistoryPage
